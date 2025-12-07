import sys
import re
import math
from itertools import accumulate as acc
from itertools import chain as flatten


def p1():
    D = open(f'{sys.argv[1]}.txt').read().strip().split('\n\n')
    D = D[0].split('\n')
    nums = {k: [] for k in range(len(D[0]))}
    sum = 0

    for i, line in enumerate(D):
        parts = [x.strip() for x in line.split(' ') if x.lstrip(' ')]
        for ii, part in enumerate(parts):
            if i == len(D) - 1:
                sum += eval(part.join(nums[ii]))
            else:
                nums[ii].append(part)
    print(sum)

def p2():
    D = open(f'{sys.argv[1]}.txt').read().strip().split('\n\n')
    D = D[0].split('\n')

    operators = []
    start = 0
    operator = '*'
    sum = 0
    for i in range(1, len(D[-1])):
        if D[-1][i] != ' ':
            operators.append((operator, start, i - 1))
            operator = D[-1][i]
            start = i
        if i == len(D[-1]) - 1:
            operators.append((operator, start, len(max(D, key=len)) - 1))

    for op, start, end in operators:
        numbers = []
        for i in range(start, end + 1):
            num = ''
            for line in D[:-1]:
                if i < len(line) and line[i] != ' ':
                    num += line[i]
            if len(num) > 0:
                numbers.append(num)
        sum += eval(op.join(numbers))
    print(sum)

p2()