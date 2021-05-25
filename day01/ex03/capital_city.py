import sys
def capital_city():
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
    ret = capital_cities.get(states.get(args[0]))
    if (ret == None):
        print("Unknown state")
        return 
    print(ret)

if __name__ == '__main__': capital_city()
