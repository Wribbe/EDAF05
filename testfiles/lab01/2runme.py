#!/usr/bin/python2.7
import sys

def main():

    input_lines = open(sys.argv[1]).readlines()

    i = 0
    for line in input_lines:
        if line.startswith('#'):
            i += 1;
            continue
        break
    input_lines = input_lines[i:]
    n = int(input_lines[0].split("=")[1])
    input_lines = input_lines[1:]

    names = []
    names.append("")

    preferences = [[]]

    doing_preferences = False
    for line in input_lines:
        line = line.strip()
        if line == "":
            doing_preferences = True
            continue
        if doing_preferences:
            preferences.append([int(x) for x in line.split(":")[1].split()])
        else:
            names.append(line.split(" ")[1])

    male_stack = []
    male_depth = [-1]

    female_current = [-1]
    male_current = [-1]

    for i in range(1,n*2,2):
        male_stack.append(i)

    for _ in range(n*2):
        male_depth.append(-1)
        female_current.append(-1)
        male_current.append(-1)

    while(len(male_stack) > 0):
        current_male = male_stack[0]
        current_depth = male_depth[current_male]
        for female_pref_id in preferences[current_male]:
       # for female_pref_id in preferences[current_male][male_depth[current_male]:]:
            male_depth[current_male] += 1
            match_id = match(current_male, female_pref_id, preferences, female_current)
            if match_id > 0:
                male_stack.append(match_id)
                male_current[match_id] = -1
            elif match_id == 0:
                continue
            male_stack.remove(current_male)
            male_current[current_male] = female_pref_id
            break

    pairs = []

    for male_id, female_id in enumerate(male_current):
        if female_id == -1:
            continue
        pairs.append((names[male_id],names[female_id]))

    for male, female in pairs:
        print "{} -- {}".format(male,female)

def match(male_id, female_id, preferences, female_current):
    current_id = female_current[female_id]
    female_preferences = preferences[female_id]
    for id in female_preferences:
        if current_id == id:
            return 0
        elif male_id == id:
            female_current[female_id] = male_id
            return current_id

if __name__ == "__main__":
    main()
