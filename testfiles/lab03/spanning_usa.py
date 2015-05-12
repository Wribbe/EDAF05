
def main():

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
            cities[start][distance] = end
    for city in cities:
        print city

    city_nodes = {}



class Node(object):

    def __init__(self, name):
        self.connections = {}
        self.name = name
        self.visited = False

    def add_connection(self,destination,distance):
        try:
            connections[distance].append(destination)
        except:
            new_list = connections[distance] = []
            new_list.append(destination)

if __name__ == "__main__":
    main()
