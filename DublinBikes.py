from bs4 import BeautifulSoup
import urllib2
import requests
import json
import csv
import time

def LoadJson():
    with requests.Session() as Session:
        Response = Session.get("http://api.citybik.es/dublinbikes.json")
        html = Response.text
        JsonData = json.loads(html)
        global JsonData
    return (JsonData)

def GetStations():
    Stations = ""
    with requests.Session() as Session:
        Response = Session.get("http://api.citybik.es/dublinbikes.json")
        html = Response.text
        j = json.loads(html)
    for x in j:
        station_number = str(x['number']).strip(" ")
        Stations += station_number+","
    return str(Stations.rstrip(","))

def GetStation(Station):
    j = JsonData
    for x in j:
        if x['number'] == int(Station):
            return(x)

def DublinBikes(q):
    Stations = q.replace(" ","").split(",")
    html = ""
    for Station in Stations:
        Json = GetStation(Station)
        Available = Json[u'bikes']
        Free = Json[u'free']
        Name = Json[u'name']
        Result += Name_of_Station[Station] + ": " + str(Available) + " bike(s) available and " + str(Free) + " station(s) free" +"\n"
    return(Result)

def DublinBikes(q):
    Stations = q.replace(" ","").split(",")
    Result = ""
    for Station in Stations:
        Json = GetStation(Station)
        Available = Json[u'bikes']
        Free = Json[u'free']
        Name = Json[u'name']
        Result += "Station Name: "+str(Name)+" | Station Number: "+str(Station)+" | Available Bikes: "+str(Available)+" | Free Stands: "+str(Free)+"\n"
    return(Result)

## EXAMPLE ##
LoadJson()
print DublinBikes("1, 2, 3")
