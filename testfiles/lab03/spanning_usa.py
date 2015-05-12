
lines = [x.strip().replace('"','') for x in open("USA-highway-miles.in").readlines()]

distances = False

cities = {}

for line in lines:
    if not distances:
        if "--" in line:
            distances = True
        else:
            cities[line] = {}
    if distances:
        start , end = line.split('--')
        tokens = end.split(" ")
        distance = tokens.pop(-1).replace("[",'').replace("]",'')
        end = " ".join(tokens)
        cities[start][end] = distance
