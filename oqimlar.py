import json
import time
from threading import Thread


import httpx as httpx

def bir():
    url1 = 'https://api.chucknorris.io/jokes/random'
    birinchi = httpx.get(url1)
    l = birinchi.json()
    with open('birinchi.json', 'w') as f:
        json.dump(l, f, indent=4)

def ikki():
    url2 = 'https://jsonplaceholder.typicode.com/photos'
    ikkinchi = httpx.get(url2)
    l = ikkinchi.json()
    with open('ikkinchi.json', 'w') as f:
        json.dump(l, f, indent=4)

def uch():
    url2 = 'https://www.boredapi.com/api/activity'
    uch = httpx.get(url2)
    l = uch.json()
    with open('uch.json', 'w') as f:
        json.dump(l, f, indent=4)

def turt():
    url2 = 'https://api.first.org/data/v1/countries'
    turt = httpx.get(url2)
    l = turt.json()
    with open('turt.json', 'w') as f:
        json.dump(l, f, indent=4)

def besh():
    url2 = 'https://jsonplaceholder.typicode.com/users'
    besh = httpx.get(url2)
    l = besh.json()
    with open('besh.json', 'w') as f:
        json.dump(l, f, indent=4)

stat = time.time()
oqim1 = Thread(target=bir(), daemon=True)
oqim2 = Thread(target=ikki(), daemon=True)
oqim3 = Thread(target=uch(), daemon=True)
oqim4 = Thread(target=turt(), daemon=True)
oqim5 = Thread(target=besh(), daemon=True)
end = time.time()
print(int(end - stat))



