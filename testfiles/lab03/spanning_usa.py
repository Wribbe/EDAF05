
def main():

    lines = [x.strip().replace('"','') for x in open("USA-highway-miles.in").readlines()]

    distances = False

    cities = {}

    for line in lines:
        if not distances:
            if "--" in line:
                distances = True
            else:
                cities[line] = Node(line)
        if distances:
            start , end = line.split('--')
            tokens = end.split(" ")
            distance = tokens.pop(-1).replace("[",'').replace("]",'')
            end = " ".join(tokens)
            cities[start].add_connection(end, distance)

    num_cities = len(cities.keys())
    print "number of cities: {}".format(num_cities)
    added = 0
    total_weight = 0
    start_key = cities.keys()[0]
    start_node = cities[start_key];
    print "starting at city {}".format(start_key)
    start_node.visited = True
    added += 1
    current_node = start_node
    while(added != num_cities):
        current_connection = current_node.pop()
        if current_connection.destination == "End":
            print "Error: Encounterd End, count was {}".format(added)
            return
        next_node = cities[current_connection.destination]
        while(next_node.visited == True): 
            current_connection = current_node.pop()
            next_node = cities[current_connection.destination]

        # the current next_node has not been visted.
        # add the current_connection.weight to total_weight
        # and mark the next_node as visited
        # make next_node into current_node

        total_weight += int(current_connection.weight)
        current_node = next_node
        current_node.visited = True
        added += 1
        print "added {} to spanning tree.".format(current_node.name)

class ListNode(object):

    def __init__(self, weight="End", destination="End", next="End"):
        self.weight = weight
        self.destination = destination
        self.next = next

class Node(object):

    def __init__(self, name):
        self.connections = ListNode()
        self.name = name
        self.visited = False

    def add_connection(self,destination,weight):
        current_connection = self.connections
        if current_connection.destination == "End":
            new_node = ListNode(weight, destination, current_connection)
            self.connections = new_node
        else:
            if(int(weight) < int(self.connections.weight)):
                new_node = ListNode(weight, destination, self.connections)
                self.connections = new_node
                return
            previous_connection = self.connections
            while(current_connection.destination != "End"):
                current_weight = int(current_connection.weight)
                new_weight = int(weight)
                if (new_weight < current_weight):
                    new_node = ListNode(weight, destination, current_connection)
                    previous_connection.next = new_node
                    return
                previous_connection = current_connection
                current_connection = current_connection.next
            previous_connection.next = ListNode(weight, destination, current_connection)

    def pop(self):
        if self.connections.destination == "End":
            return ListNode()
        else:
            temp = self.connections
            self.connections = self.connections.next
            return temp

if __name__ == "__main__":
    main()
