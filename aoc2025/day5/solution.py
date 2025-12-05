import sys
import re
import math
from itertools import accumulate as acc
from itertools import chain as flatten


def p1():
    D = open(f'{sys.argv[1]}.txt').read().strip().split('\n\n')
    ranges = []
    inventory = list(map(int, D[1].split('\n')))
    count = 0
    for line in D[0].split('\n'):
        start, end = map(int, line.split('-'))
        ranges.append((start, end))

    for n in inventory:
        for start, end in ranges:
            if start <= n <= end:
                count += 1
                break

    print(count)

def p2():
    D = open(f'{sys.argv[1]}.txt').read().strip().split('\n\n')
    ranges = []
    count = 0
    for line in D[0].split('\n'):
        start, end = map(int, line.split('-'))
        conflicting = []
        for r_start, r_end in ranges:
            if r_start <= start <= r_end or r_start <= end <= r_end or start <= r_start <= end:
                conflicting.append((r_start, r_end))

        if len(conflicting) == 0:
            ranges.append((start, end))
        else:
            min = start
            max = end
            for c_start, c_end in conflicting:
                ranges.remove((c_start, c_end))
                if c_start < min:
                    min = c_start
                if c_end > max:
                    max = c_end
            ranges.append((min, max))

    for s, e in ranges:
        count += e - s + 1


    print(count)


p1()
p2()