#!/usr/bin/env python3
import sys
import json
import dewiki
import requests


def dataRequest():
    # s = requests.Session()
    # URL = "http://en.wikipedia.org/w/api.php"
    # SEARCHPAGE = "Nelson Mandela"

    # PARAMS = {
    #     "action": "query",
    #     "format": "json",
    #     "list": "search",
    #     "srsearch": SEARCHPAGE
    # }
    # R = s.get(url=URL, params=PARAMS)
    # DATA = R.json()
    # if DATA['query']['search'][0]['title'] == SEARCHPAGE:
    #     print("Your search page '" + SEARCHPAGE + "' exists on English Wikipedia")

    S = requests.Session()
    URL = "https://en.wikipedia.org/w/api.php"
    PARAMS = {
        "action": "parse",
        "page": "Chocolate",
        "format": "json"
    }
    R = S.get(url=URL, params=PARAMS)
    DATA = R.json()
    print(DATA["parse"])
    # print(DATA["parse"]["text"])
    # print(DATA["parse"]["text"]["*"])


if __name__ == '__main__':
    dataRequest()