#!/usr/bin/python2.7

import sys
import os

def get_files():
    files = os.listdir(".")
    name_dict = {}
    for filestring in files:
        if "swp" in filestring:
            continue
        filename = filestring.split(".")[0]
        data_present = name_dict.get(filename)
        if data_present:
            data_present.append(filestring)
        else:
            name_dict[filename] = [filestring]
    return name_dict

def main(): 
    print get_files()

if __name__ == "__main__":
    main()
