from heapq import *
import math

def main():

    lines = [" ".join(x.strip().split()[1:])
             for x in open("files/rl11849.tsp").readlines()
             if x.split()[0].isdigit()]

    x_heap = []
    y_heap = []

    for num, line in enumerate(lines):
        x, y = line.split()
        x = float(x)
        y = float(y)
        heappush(x_heap, (float(x), "{},{},{}".format(num,x,y)))
        heappush(y_heap, (float(y), "{},{},{}".format(num,x,y)))

    p_x = heapsort(x_heap)
    p_y = heapsort(y_heap)

    print closest_pair_rec(p_x, p_y)

def closest_pair_rec(px, py):
    xlen = len(px)

    # px[x] = (x_pos, (num, x_pos, y_pos))

    if xlen <= 3:
        heap = []
        if xlen <= 1:
            return 0
        elif xlen == 2:
            num1, x1, y1 = px[0][1].split(',')
            num2, x2, y2 = px[1][1].split(',')
            heappush(heap, (distance(x1,x2,y1,y2), (num1, num2)))
        elif xlen == 3:
            num1, x1, y1 = px[0][1].split(',')
            num2, x2, y2 = px[1][1].split(',')
            num3, x3, y3 = px[1][1].split(',')
            heappush(heap, (distance(x1,x2,y1,y2), (num1, num2)))
            heappush(heap, (distance(x1,x3,y1,y3), (num1, num3)))
            heappush(heap, (distance(x2,x3,y2,y3), (num2, num3)))
        return_value = heappop(heap)
        return return_value
    else:
        mid = xlen/2
        min_left = closest_pair_rec(px[:mid], py[:mid])
        min_right = closest_pair_rec(px[mid:], py[mid:])

        if min_left[0] == 0.0:
            delta = min_right[0]
        elif min_right[0] == 0.0:
            delta = min_left[0]
        else:
            delta = min(min_left[0],min_right[0])

        x_max = px[mid:][-1][0]

        s = []
        for point in px:
            _, coords = point
            num, x, y = [float(token) for token in coords.split(',')]
            if abs(x_max-x) <= delta:
                heappush(s, (y, (num, x, y)))
        s = heapsort(s)

        s_min_heap = []
        for num, point in enumerate(s):
            for diff_point in s[num:15]:
                dist = pdistance(point, diff_point)
                if dist < delta and dist != 0:
                    heappush(s_min_heap, (dist, point, diff_point))

        if len(s_min_heap):
#            print "return from min_heap"
            return delta,heappop(s_min_heap)
        elif min_left[0] < min_right[0]:
#            print "return from min_left"
            return min_left
        else:
#            print "return from min_right"
            return min_right

def pdistance(point1, point2):
    num1,x1,y1 = coords(point1)
    num2,x2,y2 = coords(point2)
    return distance(x1,y1,x2,y2)

def coords(point):
    _, coords = point
    num,x,y = coords
    return num,x,y

def distance(x1,y1,x2,y2):
    x1,y1,x2,y2 = [float(num) for num in [x1,y1,x2,y2]]
    dist = math.sqrt(pow(x2-x1,2) + pow(y2-y1,2))
    if dist == 0.0:
        print "Returning 0.0..."
    return dist

def heapsort(heap):
    return [heappop(heap) for _ in range(len(heap))]

if __name__ == "__main__":
    main()
