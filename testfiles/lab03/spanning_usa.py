
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
    current_path = []
    total_weight = 0
    start_key = cities.keys()[0]
    start_node = cities[start_key];
    print "starting at city {}".format(start_key)
    start_node.visited = True
    added += 1
    current_path.append(start_node)
    current_node = start_node
    previous_node = current_node
    while(added != num_cities):
        current_connection = current_node.pop()
        while(current_connection.destination == "End"):
            current_connection = back_up(current_path)
        next_node = cities[current_connection.destination]
        while(next_node.visited == True): 
            current_connection = current_node.pop()
            while (current_connection.destination == 'End'):
                print "there was only a dead end at {}, backing up".format(current_node.name)
                current_connection = back_up(current_path)
            print "Already visited {}, trying {}".format(next_node.name, current_connection.destination)
            next_node = cities[current_connection.destination]

        # the current next_node has not been visted.
        # add the current_connection.weight to total_weight
        # and mark the next_node as visited
        # make next_node into current_node

        total_weight += int(current_connection.weight)
        previous_node = current_node
        current_node = next_node
        current_node.visited = True
        added += 1
        current_path.append(current_node)
        print "added {} to spanning tree.".format(current_node.name)

def back_up(node_path):
    print [x.name for x in node_path]
    dead_end = node_path.pop(-1) # get rid of current dead end.
    previous_city = node_path.pop(-1)
    current_connection = previous_city.pop()
    while(current_connection.destination == "End"):
        dead_end = previous_city
        previous_city = node_path.pop(-1)
        print "Error: Encounterd End at {}, backing up to {}".format(dead_end.name,previous_city.name)
        current_node = previous_city
        current_connection = current_node.pop()
    print "returning connection to {}, from {}".format(current_connection.destination, previous_city.name)
    return current_connection


def print_list_node(node):
    list_node = node.connections
    while(list_node.next != "End"):
        print "{} : {}".format(list_node.destination, list_node.weight)
        list_node = list_node.next

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
