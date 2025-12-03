import sys
import re
import math
from itertools import accumulate as acc
from itertools import chain as flatten


def p1():
    D = open(f'{sys.argv[1]}.txt').read().strip().split('\n\n')

    joltage = 0
    for line in D[0].split('\n'):
        num = 0
        nums = [int(x) for x in line]
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                new_num = int(str(nums[i]) + str(nums[j]))
                if new_num > num:
                    num = new_num
        joltage += num

    print(joltage)

def p2():
    D = open(f'{sys.argv[1]}.txt').read().strip().split('\n\n')

    joltage = 0
    for line in D[0].split('\n'):
        num = ''
        for i in range(11, -1, -1):
            nums = [int(x) for x in line[:len(line)-i]]
            max_num = max(nums)
            num += str(max_num)
            line = line[line.index(str(max_num)) + 1:]

        joltage += int(num)

    print(joltage)


p1()
p2()