#!/usr/bin/env python3
import sys
import requests
from bs4 import BeautifulSoup 

def roadsToPhilosophy(searchWord, count):
    S = requests.Session()
    URL = "https://en.wikipedia.org/" + searchWord
    try:
        f = "None"
        res = S.get(url=URL)
        if res.status_code != 200 :
            raise Exception("It leads to a dead end !")
        soup = BeautifulSoup(res.text, 'html.parser')
        if (count == 1):
            f =  soup.find(id='firstHeading').text
        dsoup = soup.find(id='mw-content-text')
        href = dsoup.select_one('p > a')
        r = str(href).split('href="')[1]
        r = r.split('"')[0]
        return r, f
    except Exception as err:
        raise SystemExit(err)
def walk():
    try:
        count = 1
        if len(sys.argv) != 2:
            raise InputError("Input is {} words".format(len(sys.argv) - 1))
        if sys.argv[1] == "Philosophy" or sys.argv[1] == "philosophy":
            print("Philosophy\n1 roads from Philosophy to philosophy !")
            exit(0)
        wordList = []
        searchWord = "wiki/" + sys.argv[1]
        while searchWord != '/wiki/Philosophy':
            searchWord, f = roadsToPhilosophy(searchWord, count)
            if searchWord in wordList:
                raise Exception("It leads to an infinite loop !")
            else:
                wordList.append(searchWord)
            if count == 1 : 
                print(f)
                wordList.append("/wiki/" + f)
            count+=1
            print(searchWord.split("/")[2])
        print("{} roads from {} to philosophy !".format(count, sys.argv[1]))
    except Exception as e:
        print(e)

if __name__ == "__main__":
    walk()