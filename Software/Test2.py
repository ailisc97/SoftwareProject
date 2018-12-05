import csv
import requests
from bs4 import BeautifulSoup
import time

while True:
    url = 'http://www.dublincity.ie/dublintraffic/cpdata.xml?1543254514266'

    res = requests.get(url)
    soup = BeautifulSoup(res.content,"xml")
    data = []
    for item in soup.select("carpark"):
        ditem = {}
        ditem['Name'] = item.get("name")
        ditem['Spaces'] = item.get("spaces")
        data.append(ditem)

    with open("CarparkData.csv","w",newline="") as f:
        writer = csv.DictWriter(f,["Name","Spaces"])
        writer.writeheader()
        for info in data:
            writer.writerow(info)

    time.sleep(5 * 60)