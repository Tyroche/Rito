import urllib3
import certifi
import json
import re
from pprint import pprint

class DataCollector:

    #init
    def __init__(self,matchid,region,items=False):
        self._matchid = matchid
        self._region  = region

        with open("key.txt") as infile:
            self._api_key = infile.read()
        self._include_timeline = "false"

        #Create URL for search

        if items is False:
            self._url = "https://na.api.pvp.net/api/lol/{}/v2.2/match/{}?includeTimeline={}&api_key={}".format(self._region, self._matchid, self._include_timeline,self._api_key)
        else:
            self._url = "https://global.api.pvp.net/api/lol/static-data/na/v1.2/item?api_key={}".format(self._api_key)

        self.fetchData()

    #Returns request object that can be queried for data
    def fetchData(self):
        http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
        self._r = http.request('GET', self._url)

        if self._r.status != 200:
            print("Something went wrong getting the files!")
            exit()

    #Prints matchid data
    def printData(self):
        if not self._r:
            print("Need to run fetchData first")
            exit()

        print(self._r.data.decode('UTF-8'))

    def getData(self):
        return(self._r.data.decode('UTF-8'))

    def getJSON(self):
        return json.loads(self._r.data.decode('UTF-8'))


