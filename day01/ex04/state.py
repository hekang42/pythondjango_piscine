import sys
def state():
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
    abb_find = None
    for abb, capital_city in capital_cities.items():
        if (args[0] == capital_city):
            abb_find = abb
    if (abb_find == None):
        print("Unknown capital city")
        return 
    for state, abb in states.items():
        if (abb_find == abb):
            ret = state
    print(ret)
if __name__ == '__main__': state()
