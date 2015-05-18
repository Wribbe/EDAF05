from heapq import *

def main():

    lines = [" ".join(x.strip().split()[1:])
             for x in open("files/rl11849.tsp").readlines()
             if x.split()[0].isdigit()]

    x_heap = []
    y_heap = []
    for num, line in enumerate(lines):
        x, y = line.split()
        heappush(x_heap, (float(x), num))
        heappush(y_heap, (float(y), num))

    print heapsort(x_heap)

def heapsort(heap):
    return [heappop(heap) for _ in range(len(heap))]

if __name__ == "__main__":
    main()
