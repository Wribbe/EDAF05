from closest_pair import find
import os
import sys

import cProfile

correct_outputs_raw = [x.strip() for x in open('files/closest-pair.out').readlines()]
ans_tokens = [line.replace('../data/','').replace(':','').split() for line in correct_outputs_raw]
ans_tuples = []

if "--profile" in sys.argv:
    cProfile.run('find("files/brd14051.tsp")')
    sys.exit()

for tokens in ans_tokens:
    ans_tuples.append((tokens[0],tokens[2]))

for filename in os.listdir('files/wc'):
    print "result for {}: {}".format(filename,find("files/wc/{}".format(filename)))

for tup in ans_tuples:
    filename, ans = tup
    result = find("files/{}".format(filename))
    cut = 10
    ans = str(float(ans))[:cut].strip()
    len_ans = len(str(ans))
    result = str(result)[:cut].strip()
    if (ans == result):
        print "distance is CORRECT for {}!".format(filename)
    else:
        print "distance is NOT correct for {}!".format(filename)
        print "result: {} len: {}".format(result, len(result))
        print "ans: {} len: {}".format(ans, len(ans))

