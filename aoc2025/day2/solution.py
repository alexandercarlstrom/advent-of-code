import sys
import re
import math
from itertools import accumulate as acc
from itertools import chain as flatten


def p1():
    D = open(f'{sys.argv[1]}.txt').read().strip()
    ranges = [r.split('-') for r in D.split(',')]


    invalid = 0
    for r in ranges:
        a, b = int(r[0].strip()), int(r[1].strip())

        for n in range(a, b + 1):
            if str(n)[:len(str(n)) // 2] == str(n)[len(str(n)) // 2:]:
              invalid += n

    print(invalid)


def p2():
    D = open(f'{sys.argv[1]}.txt').read().strip()
    ranges = [r.split('-') for r in D.split(',')]
    invalid = 0
    for r in ranges:
        a, b = int(r[0].strip()), int(r[1].strip())

        for n in range(a, b + 1):
            n_str = str(n)

            for i in range(len(n_str)):
                part = n_str[:i + 1]
                if part * (len(n_str) // len(part)) == n_str and n_str != part:
                    invalid += n
                    break

    print(invalid)


p2()
