import json
import requests
from requests.exceptions import ConnectionError
data = json.load(open('file.json'))


# 1. skrypt 1 csv -> json
# 2. json -> klasy do klasyfikatora
# 3. klasyfikacja bayesem
#grupowac po '#' , tabele na podtabele

tmp = 0

for row in data["content"]:
    tmp += 1

tab = []
tab.append("172.21.0.2:5000")
tab.append("172.21.0.3:5000")
tab.append("172.21.0.4:5000")
ilosc = len(tab)
tmp2 = tmp / ilosc
tmp = 0
tmp3 = 0


def checkContainersAvailability():
    areNotAvailable = True

    while areNotAvailable:
        try:
            requests.get("http://" + tab[0] + "/ping")
            requests.get("http://" + tab[1] + "/ping")
            requests.get("http://" + tab[2] + "/ping")
        except ConnectionError as e:
            print("Some workers are still unavailable")
            continue
        areNotAvailable = False

    print("Workers are available")


checkContainersAvailability()


for row in data["content"]:
    r = requests.post('http://' + tab[tmp3] + '/add', json.dumps(row))
#    print(r.text)
    tmp3 += 1

    if tmp3 == ilosc:
        tmp3 = 0
        pliktmp = {}

response = requests.get('http://' + tab[0] + '/test1')
print("Workers are currently learned")
