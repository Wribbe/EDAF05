lines = [" ".join(x.strip().split()[1:])
         for x in open("files/rl11849.tsp").readlines() if x.split()[0].isdigit()]

for line in lines:
    x, y = line.split()
    print "{},{}".format(float(x),float(y))
