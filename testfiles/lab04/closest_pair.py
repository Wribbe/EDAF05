import math
from heapq import *
import sys

def find(filename):
    lines = parse_input(filename)
    points = []
    for num, line in enumerate(lines):
        points.append(Point("{} {}".format(num,line)))

    sorted_x = sortx(points)
    sorted_y = sorty(points)

    result = min_distance_recursive(sorted_x, sorted_y)
    if "wc" in filename:
        return "distance: {} -- P{} <--> P{}".format(result.distance, result.p1.num, result.p2.num)
    return result.distance

def min_distance_recursive(sorted_x, sorted_y):

    if len(sorted_x) <= 3:
        dist = min_dist_3p(sorted_x, print_dist=False)
        return dist

    mid_x, left_x, right_x = split_list(sorted_x)

    left_y, right_y = split_y(mid_x, sorted_y)

    min_dist_left = min_distance_recursive(left_x, left_y)
    min_dist_right = min_distance_recursive(right_x, right_y)

    delta_dist = get_delta(min_dist_left, min_dist_right)
    delta = delta_dist.distance

    max_x = left_x[-1]

    l_distances = distances_around_l(max_x, delta, left_x+right_x, left_y+right_y)
    if l_distances:
        return l_distances[0]
    elif min_dist_left.distance < min_dist_right.distance:
        return min_dist_left
    else:
        return min_dist_right

def min_dist_3p(points, print_dist=False):
    heap = []
    for num, point in enumerate(points):
        for second_point in points[num+1:]:
            distance = point.distance(second_point)
            push_dist(heap, distance)
    if len(heap) == 0:
        return Distance(-1, None, None)
    return pop_dist(heap)

def split_list(point_list):
    mid = len(point_list)/2
    mid_point = point_list[mid]
    return mid_point.x, point_list[:mid], point_list[mid:]

def split_y(mid_x, sorted_y):
    left = []
    right = []
    for point in sorted_y:
        if point.x <= mid_x:
            left.append(point)
        else:
            right.append(point)
    return left, right

def get_delta(distance1, distance2):

    dist1 = distance1.distance
    dist2 = distance2.distance

    if dist1 < dist2:
        return distance1
    else:
        return distance2

def distances_around_l(max_x, delta, points, ypoints):
    distance_heap = []
    increment = 15
    points = points_around_l(max_x, delta, ypoints)
    for num, point in enumerate(points):
        second_start = num+1 # Don't compare to your selfe
        for second_point in points[second_start:second_start+increment]:
            distance = point.distance(second_point)
            if distance.distance < delta:
                push_dist(distance_heap, distance)
    return [pop_dist(distance_heap) for _ in range(len(distance_heap))]

def points_around_l(max_x, delta, points):
    y_points = []
    for point in points:
        if point.x - max_x.x < delta:
            y_points.append(point)
    return y_points


#-----------------------------------------------------------------------
#-- Classes
#-----------------------------------------------------------------------

class Point(object):

    def __init__(self, coords):
        num, x, y = [float(coord) for coord in coords.split()]
        self.num = int(num)
        self.x = x
        self.y = y

    def distance(self, point):
        diffx = self.x-point.x
        diffy = self.y-point.y
        dist = Distance(math.sqrt(diffx**2+diffy**2),
                        self,
                        point)
        return dist #58.841

    def __repr__(self):
        return "P{}: x:{} y:{}".format(self.num, self.x, self.y)

class Distance(object):

    def __init__(self, distance, point1, point2):
        self.distance = distance
        self.p1 = point1
        self.p2 = point2

    def __repr__(self):
        return "Distance: {} -- {} <--> {}".format(self.distance, self.p1, self.p2)

    def heap_format(self):
        return self.distance, self

    def info(self):
        print "Point#{} <--> Point#{} = {}".format(self.p1.num,
                                                   self.p2.num,
                                                   self.distance)

#-----------------------------------------------------------------------
#-- Utility
#-----------------------------------------------------------------------

def push_dist(heap, distance):
    heappush(heap, distance.heap_format())

def pop_dist(heap):
    return heappop(heap)[1]

def parse_input(filename):
    lines = [x.strip() for x in open(filename).readlines()]
    only_numerals = []
    for line in lines:
        if line == "":
            continue
        tokens = line.split()
        if len(tokens) < 3:
            continue
        try:
            if tokens[0].isdigit():
                only_numerals.append(" ".join(tokens[1:]))
        except:
            import pudb; pu.db
    return only_numerals


def sortx(point_list):
    return sort_utils('x', point_list)

def sorty(point_list):
    return sort_utils('y', point_list)

def sort_utils(key, point_list):
    heap = []
    for point in point_list:
        if key == 'x':
            heappush(heap, (point.x, point))
        else:
            heappush(heap, (point.y, point))
    return [pop_dist(heap) for _ in range(len(heap))]
