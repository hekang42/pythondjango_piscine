#!/usr/bin/python3
import sys, re, os

def make_dict():
    with open("./settings.py", 'r') as myfile:
        settings = myfile.readlines()
    dset = {}
    for line in settings:
        if (line == '\n'):
            continue
        words = line.split("=")
        if (len(words) != 2):
            continue
        words[0] = words[0].strip()
        words[1] = words[1].strip().replace('"','').replace("\n","")
        dset[words[0]] = words[1]
    return dset

def get_template(template_name):
    if os.path.isfile(template_name):
        with open("./" + template_name, 'r') as myfile:
            s = myfile.read()
    else :
        return -1
    return s

def check_template(template_name):
    if (template_name[-8:] != "template"):
        return -1
    return 1

def write_string(s, template_name):
    f = open("./" + template_name[:-9] + ".html", 'w')
    f.write(s)
    f.close()

def ft_replace():
    args = sys.argv[1:]
    if (len(args) != 1):
        print("Error: Argument is only 1")
        return
    template_name = args[0]
    dset = make_dict()
    if (check_template(template_name) == -1):
        print("Error: Not a template file")
        return 
    html_string = get_template(template_name)
    if (html_string == -1):
        print("Error: template file does not exist")
        return
    for key in dset:
        to_find = "\\{(" + key + ")\\}"
        html_string = re.sub(to_find, dset[key], html_string)
    write_string(html_string, template_name)

if __name__ == '__main__':ft_replace()