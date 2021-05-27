#!/usr/bin/python3
import antigravity
import sys

def get_geohash():
    arg = sys.argv
    try:
        if len(arg) != 4:
            raise ValueError("To many or little Arguments")
        antigravity.geohash(latitude = float(arg[1]), longitude= float(arg[2]), datedow = arg[3].encode())
    except ValueError as e:
        print("Error : In arguments(float float string).\tError description: {}".format(e))
    except Exception as e:
        print("Error : Unknown.\tdescription: {}".format(e))


if __name__ == '__main__':
    get_geohash()


#./geohashing.py 37.42154 -122.0385589 "2005-05-26-10458.68"