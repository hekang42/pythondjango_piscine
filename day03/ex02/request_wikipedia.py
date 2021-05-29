#!/usr/bin/env python3
import sys
import json
import dewiki
import requests

class InputError(Exception):
    pass

def dataRequest():
    try:
        if (len(sys.argv) != 2):
            raise InputError("Input is {} words".format(len(sys.argv) - 1))
        searchWord = sys.argv[1]
        searchWord.replace(" ", "_")

        S = requests.Session()
        URL = "https://en.wikipedia.org/w/api.php"
        PARAMS = {
            "action": "parse",
            "page": searchWord,
            "prop": "wikitext",
            "format": "json",
            "redirects": True
        }
        res = S.get(url=URL, params=PARAMS)
        data = res.json()
        if (dict(data).get("error") != None):
            raise ValueError(data["error"])
        wikitext = data['parse']['wikitext']["*"]
        destring = dewiki.from_string(wikitext)

        # destring = destring.replace("|","").replace("\n ","\n").replace("\n\n", "\t")
        
        with open("./" + searchWord.replace(' ', '_') + ".wiki", 'w') as myfile:
            myfile.write(destring)
            myfile.close

    except InputError as e:
        print("Error ***** Input only 1 word {}".format(e))
    except ValueError as e:
        print("{} cannot find anything in wiki.en".format(searchWord))
    except Exception as e:
        print("Error : Unknown.\tdescription: {}".format(e))

if __name__ == '__main__':
    dataRequest()