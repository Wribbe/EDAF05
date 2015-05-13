
def main():

    cities = parse_input()

    start_city = cities.keys()[0]

    print "starting in {}".format(start_city)

    start_node = cities[start_city]
    start_node.visited = True

    current_path = [start_node]
    current_node = start_node
    while(True):
        next_connection = current_node.pop()
        next_destination = next_connection.destination
        if cities[next_destination].connections.destination == "End":
            print "Theres is only a dead end at {}".format(cities[next_destination].name)
            print [x.name for x in current_path]
            break
        else:
            current_node = cities[next_destination]
            current_path.append(current_node)
        print "next connection is to {}.".format(next_destination)


def parse_input():

    cities = {}
    lines = [x.strip().replace('"','') for x in open("USA-highway-miles.in").readlines()]
    distances = False
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
    return cities

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
