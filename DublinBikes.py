from bs4 import BeautifulSoup
import urllib2
import requests
import json
import csv
import time

def load_csv_file(name="data"):
    dict = {}
    for x in range(0,999):
        dict[x] = "Station Number "+str(x)
    filename = name+".csv"
    with open(filename, 'rb') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            station_name = row[1]
            station_number = row[0]
            dict[station_number] = station_name
    return dict
    
def DublinBikes(q):
    Name_of_Station = load_csv_file()
    Stations = q.replace(" ","").split(",")
    Result = ""
    with requests.Session() as Session:
        for Station in Stations:
            try:
                Text = ""
                while Text == "":
                    time.sleep(1)
                    Response = Session.get('http://www.dublinbikes.ie/service/stationdetails/dublin/'+str(Station), data={})
                    Text = Response.text
                    try:
                        Soup = BeautifulSoup(Text, "lxml")
                    except:
                        Soup = BeautifulSoup(Text)
                    Available = Soup.find("available").text
                    Free = Soup.find("free").text
                    Total = Soup.find("total").text
                    Ticket = Soup.find("ticket").text
                    Open = Soup.find("open").text
                    Updated = Soup.find("updated").text
                    Connected = Soup.find("connected").text
                    Result += Name_of_Station[Station] + ": " + str(Available) + " bike(s) available and " + str(Free) + " station(s) free" +"\n"
                except:
                    pass
    return(Result.rstrip("\n"))

print DublinBikes("1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,23,24,25,26,40,41,45,47,48,49,54,55,57,59,61,62,63,65,68,69,70,71,72,73,75,76,78,79,84,87,88,89,90,92,93,94,97,99,100,101")
