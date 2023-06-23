import csv
import time
import requests
import json

mockList = []
with open("./MOCK_DATA.csv", 'r') as file:
  csvreader = csv.reader(file)
  next(csvreader)

  for row in csvreader:
    mockDic = {}
    mockDic["login"] = str(row[0])
    mockDic["password"] = str(row[1])
    mockList.append(mockDic)

list_number = 0
URL = "http://localhost:8081/api/gen"

for record in mockList:
    resp = requests.post(URL, json=json.dumps(record))
    print(resp)
    time.sleep(10)

