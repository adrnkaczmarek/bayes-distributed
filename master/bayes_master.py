import json
import requests
import time
from requests.exceptions import ConnectionError


data = json.load(open('file.json'))
tmp = 0

for row in data["content"]:
    tmp += 1

work_endpoints = []
work_endpoints.append("172.21.0.2:5000")
work_endpoints.append("172.21.0.3:5000")
work_endpoints.append("172.21.0.4:5000")
ilosc = len(work_endpoints)
tmp2 = tmp / ilosc
tmp = 0
tmp3 = 0


def checkContainersAvailability():
    areNotAvailable = True

    while areNotAvailable:
        try:
            requests.get("http://" + work_endpoints[0] + "/ping")
            requests.get("http://" + work_endpoints[1] + "/ping")
            requests.get("http://" + work_endpoints[2] + "/ping")
        except ConnectionError as e:
            print("Some workers are still unavailable")
            time.sleep(1)
            continue
        areNotAvailable = False

    print("Workers are available")


checkContainersAvailability()


for row in data["content"]:
    r = requests.post('http://' + work_endpoints[tmp3] + '/add', json.dumps(row))
    tmp3 += 1

    if tmp3 == ilosc:
        tmp3 = 0
        pliktmp = {}

response = requests.get('http://' + work_endpoints[0] + '/test1')
print("Workers are currently learned")
