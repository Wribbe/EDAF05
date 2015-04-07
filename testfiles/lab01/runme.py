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

def main(): 

if __name__ == "__main__":
    main()
