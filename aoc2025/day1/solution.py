import sys
import re
import math
from itertools import accumulate as acc


def p1():
    D = open(f'{sys.argv[1]}.txt').read().strip().split('\n\n')

    dial = 50
    count = 0
    for line in D[0].split('\n'):
        dir = line[:1]
        num = int(line[1:])
        if dir == 'R':
            dial = (dial + num) % 100
        if dir == 'L':
            dial = (dial - num) % 100

        if dial == 0:
            count += 1

    print(count)


def p2():
    D = open(f'{sys.argv[1]}.txt').read().strip().split('\n\n')

    dial = 50
    count = 0
    for line in D[0].split('\n'):
        dir = line[0]
        num = int(line[1:])
        for _ in range(num):
            if dir == 'R':
                dial = (dial + 1) % 100
            if dir == 'L':
                dial = (dial - 1) % 100

            if dial == 0:
                count += 1

    print(count)


p2()
