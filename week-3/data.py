import urllib.request as taipei
import json
import csv

src="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
with taipei.urlopen(src) as taipei_source:
    data=json.load(taipei_source)
data_allList=data["result"]["results"]

output=[]
for i in data_allList:
    if int(i["xpostDate"][0:4]) >= 2015:
        first_pic="https"+i["file"].split("https")[1]
        output.append([i["stitle"],i["address"][5:8],i["longitude"],i["latitude"],first_pic])

with open ("data.csv", "w", newline="", encoding="utf-8") as file:
    writer=csv.writer(file)
    writer.writerows(output)



    
    
    
