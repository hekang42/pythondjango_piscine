#!/usr/bin/python3
def my_numbers():
    myfile = open("numbers.txt", 'r')
    lines = myfile.readline()
    lines = lines.strip()
    strings = lines.split(",")
    for i in strings:
        print(i)
    myfile.close()
if __name__ == '__main__': my_numbers()