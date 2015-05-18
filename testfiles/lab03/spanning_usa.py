import heapq

def main():

    cities = parse_input()
    current_city = cities.keys()[0]
    visited = set()

    num_cities = len(cities)
    total_weight = 0

    new_heap = []

    # add fist cities connections to new_heap
    for distance, next_city in cities[current_city][1]:
        heapq.heappush(new_heap, (distance, next_city))

    visited.add(current_city)

    # data structure ("CityName",heap_list)

    while(len(visited) != num_cities):
        distance, next_city = heapq.heappop(new_heap)
        while(next_city in visited):
            distance, next_city = heapq.heappop(new_heap)
        total_weight += distance
        current_city = next_city
        for distance, next_city in cities[current_city][1]:
            heapq.heappush(new_heap, (distance, next_city))
        visited.add(current_city)

    print total_weight

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
