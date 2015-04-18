import sys

lines1 = [x.strip() for x in open(sys.argv[1]).readlines()]
lines2 = [x.strip() for x in open(sys.argv[2]).readlines()]

equal = True
for line1, line2 in zip(lines1,lines2):
    if line1 != line2:
        print "File {} and {} are not equal!".format(sys.argv[1], sys.argv[2])
        print "Mismatch between {} and {}.".format(line1, line2)
        equal = False
        break
if equal:
    print "File {} and {} are equal!".format(sys.argv[1], sys.argv[2])
