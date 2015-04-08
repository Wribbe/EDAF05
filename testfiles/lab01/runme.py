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
        for line in lines:
            if line.startswith("#") or line.startswith("\n") or "n=" in line:
                continue
            tokens = line.split(" ")
            head = tokens[0]
            rest = tokens[1:]
            if ":" not in head:
                names[head] = {'name': rest[0].strip()}
            else:
                head = head.replace(':','')
                names[head]["preference"] = rest
        male = {} 
        female = {}
        for key, data in names.iteritems():
            if int(key)%2 != 0:
                male[key] = data
            else:
                female[key] = data
        return male,female

def match(man_id, woman_id, females):
    current_woman = females[woman_id]
    current_man = current_woman.get("current")
    if current_man == None:
        current_woman["current"] = man_id
        return True, None
    else:
        for pref_id in current_woman["preference"]:
            if current_man in pref_id:
                return False, None
            if man_id in pref_id:
                return True, current_man

def pair_up(males, females):
    available_men = males.keys()
    while(len(available_men) != 0): 
        current_man = available_men[0]
        for woman_id in males[current_man]["preference"]:
            did_match, current = match(current_man, woman_id, females)
            if did_match:
                males[current_man]["current"] = woman_id
                available_men.remove(current_man)
                if current:
                    available_men.append(current)
                break
            continue

def fancy_print(males, females):
    for _, data in males.iteritems():
        print "{} -- {}".format(data["name"],females[data["current"]]["name"])

def main(): 
    input_filename = sys.argv[1]
    males, females = parse_input(input_filename) 
    pair_up(males,females)
    fancy_print(males, females)

if __name__ == "__main__":
    main()
