
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

    san_diego_node = cities['San Diego'].connections
    current_node = san_diego_node
    while(True):
        print "{} : {}".format(current_node.destination, current_node.weight)
        current_node = current_node.next
        if current_node == "End":
            break;

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


if __name__ == "__main__":
    main()
