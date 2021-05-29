#!/usr/bin/env python3
import sys
import requests
from bs4 import BeautifulSoup 

def roadsToPhilosophy(searchWord):
    S = requests.Session()
    URL = "https://en.wikipedia.org/" + searchWord
    try:
        res = S.get(url=URL)
        if res.status_code != 200 :
            raise Exception("It leads to a dead end !")
        soup = BeautifulSoup(res.text, 'html.parser')
        dsoup = soup.find(id='mw-content-text')
        href = dsoup.select_one('p > a')
        r = str(href).split('href="')[1]
        r = r.split('"')[0]
        return r
    except Exception as err:
        raise SystemExit(err)
def walk():
    
    try:
        count = 0
        wordList = []
        if len(sys.argv) != 2:
            raise InputError("Input is {} words".format(len(sys.argv) - 1))
        if sys.argv[1] == "Philosophy":
            print("0 roads from Philosophy to philosophy !")
            exit(0)
        searchWord = "wiki/" + sys.argv[1]
        while searchWord != '/wiki/Philosophy':
            searchWord = roadsToPhilosophy(searchWord)
            if searchWord in wordList:
                raise Exception("It leads to an infinite loop !")
            else:
                wordList.append(searchWord)
            count+=1
            print(searchWord.split("/")[2])
        print("{} roads from {} to philosophy !".format(count, sys.argv[1]))
    except Exception as e:
        print(e)

if __name__ == "__main__":
    walk()