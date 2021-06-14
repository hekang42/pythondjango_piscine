#!/usr/bin/python3
import sys

def capital_city(states, capital_cities, state_tofind):
    ret = capital_cities.get(states.get(state_tofind))
    if (ret == None):
        return None
    return ret

def state(states, capital_cities, city):
    args = sys.argv[1:]
    if (len(args) != 1):
        return 
    abb_find = None
    for abb, capital_city in capital_cities.items():
        if (city.upper() == capital_city.upper()):
            abb_find = abb
    if (abb_find == None):
        return None
    for state, abb in states.items():
        if (abb_find == abb):
            ret = state
    return (ret)

def find_all():
    states = {
        "Oregon" : "OR",
        "Alabama" : "AL",
        "New Jersey": "NJ",
        "Colorado" : "CO"
    }
    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }
    args = sys.argv[1:]
    if (len(args) != 1):
        return
    arg_list = args[0].split(",")
    for i in arg_list:
        to_find = i.strip()
        if to_find == "":
            continue
        origin_to_find = to_find
        to_find = to_find.split(" ")
        camel_to_find = ""
        for word in to_find:
            s = "".join(word[0].upper() + word[1:].lower())
            camel_to_find = camel_to_find + s + " "
        camel_to_find = camel_to_find.strip()
        state_tofind = state(states, capital_cities, camel_to_find)
        if (state_tofind == None):
            state_tofind = camel_to_find
            city = capital_city(states, capital_cities, state_tofind)
        else :
            city = camel_to_find
        if (state_tofind != None) & (city != None):
            print (city, "is the capital of", state_tofind)
        else :
            print (origin_to_find, "is neither a capital city nor a state")

if __name__ == '__main__': find_all()