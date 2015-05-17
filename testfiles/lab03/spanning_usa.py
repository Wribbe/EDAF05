import heapq

def main():

    cities = parse_input()
    starting_city = cities.keys()[0]
    visited = set()



def parse_input():

    cities = {}
    lines = [x.strip().replace('"','') for x in open("USA-highway-miles.in").readlines()]
    parsing_distances = False
    for line in lines:
        if '--' in line:
            parsing_distances = True
        if parsing_distances:
            start, tokens = line.split('--')
            tokens = tokens.split()
            distance = tokens.pop(-1).replace('[','').replace(']','')
            end = " ".join(tokens)
            heapq.heappush(cities[start][1], (int(distance), end))
            heapq.heappush(cities[end][1], (int(distance), start))
        else:
            cities[line] = (line, [])
    return cities

if __name__ == "__main__":
    main()
