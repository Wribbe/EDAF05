import math
from heapq import *

def main():
    lines = parse_input("testinput")
    points = []
    for num, line in enumerate(lines):
        points.append(Point("{} {}".format(num,line)))
    min_dist = calc_3dist(points)

    print min_dist

def calc_3dist(points):
    heap = []
    for num, point in enumerate(points):
        for second_point in points[num+1:]:
            distance = point.distance(second_point)
            push_dist(heap, distance)
    return heappop(heap)

def push_dist(heap, distance):
    heappush(heap, distance.heap_format())

def parse_input(filename):
    return [x.strip() for x in open(filename).readlines()]

class Point(object):

    def __init__(self, coords):
        num, x, y = [float(coord) for coord in coords.split()]
        self.num = int(num)
        self.x = float(x)
        self.y = float(y)

    def distance(self, point):
        return Distance(math.sqrt(math.pow(self.x-point.x,2)+math.pow(self.y-point.y,2)),
                        self,
                        point)

    def __repr__(self):
        return "{}: x:{} y:{}".format(self.num, self.x, self.y)

class Distance(object):

    def __init__(self, distance, point1, point2):
        self.distance = distance
        self.p1 = point1
        self.p2 = point2

    def __repr__(self):
        return "Distance: {} -- P1: {} <--> P2: {}".format(self.distance, self.p1, self.p2)

    def heap_format(self):
        return self.distance, (self.p1, self.p2)

    def info(self):
        print "Point#{} <--> Point#{} = {}".format(self.p1.num,
                                                   self.p2.num,
                                                   self.distance)
if __name__ == "__main__":
    main()
