from bs4 import BeautifulSoup
import urllib2
import requests
import json
import csv
import time

def LoadDict():
    dict = {}
    with requests.Session() as Session:
        Response = Session.get("http://www.dublinbikes.ie/service/carto")
        Page = Response.text
        Soup = BeautifulSoup(Page)
        for tag in Soup.findAll("marker"):
            station_name = tag["name"]
            station_number = tag["number"]
            dict[station_number] = station_name
    Session.cookies.clear()
    return dict

def GetStation(Station):
    with requests.Session() as Session:
        Response0 = Session.get("http://www.dublinbikes.ie/All-Stations/Station-map?KeyWords="+str(Station))
        Response1 = Session.get("http://www.dublinbikes.ie/ezjscore/call/ezjsc%3A%3Atime")
        Response2 = Session.get("http://www.dublinbikes.ie/service/stationdetails/dublin/" + str(Station))
        Response3 = Session.get("http://www.dublinbikes.ie/service/stationdetails/dublin/" + str(Station))
        Text = Response3.text
    return(Text)

def DublinBikes(q):
    Name_of_Station = LoadDict()
    Stations = q.replace(" ","").split(",")
    Result = ""
    for Station in Stations:
        Page = GetStation(Station)
        Soup = BeautifulSoup(Page)
        Available = Soup.find("available").text
        Free = Soup.find("free").text
        Total = Soup.find("total").text
        Ticket = Soup.find("ticket").text
        Open = Soup.find("open").text
        Updated = Soup.find("updated").text
        Connected = Soup.find("connected").text
        Result += Name_of_Station[Station] + ": " + str(Available) + " bike(s) available and " + str(Free) + " station(s) free" +"\n"
    return(Result.rstrip("\n"))

# Load and print all stations:
Stations = ""
for Station in LoadDict():
    Stations += Station+","
Stations = Stations.rstrip(",")
print DublinBikes(Stations)
