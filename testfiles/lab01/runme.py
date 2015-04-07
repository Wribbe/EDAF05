#!/usr/bin/python2.7

import sys
import os

def get_files():
    files = os.listdir(".")
    name_dict = {}
    for filestring in files:
        if "runme" in filestring:
            continue
        filename = filestring.split(".")[0]
        data_present = name_dict.get(filename)
        if data_present:
            data_present.append(filestring)
        else:
            name_dict[filename] = [filestring]
    return name_dict

def compare(lines1, lines2):
    for line1, line2 in zip(lines1,lines2):
        if line1 == line2:
            continue
        else:
            return False
    return True

def parse_input(filename):
    with open(filename) as handle:
        names = {}
        lines = handle.readlines()
        n = lines[0]
        lines = lines[1:]
        for line in lines:
            if line.startswith("#") or line.startswith("\n"):
                continue
            tokens = line.split(" ")
            head = tokens[0]
            rest = tokens[1:]
            if len(head) == 1:
                names[head] = {'name': rest}
        return names

def main(): 
    names = parse_input("sm-friends.in") 
    print names

if __name__ == "__main__":
    main()
