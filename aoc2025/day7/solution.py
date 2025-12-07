import sys
import re
import math
from itertools import accumulate as acc
from itertools import chain as flatten


def p1():
    D = open(f'{sys.argv[1]}.txt').read().strip().split('\n\n')
    G = [list(row) for row in D[0].split('\n')]
    S = (0, 0)

    for y in range(len(G)):
        for x in range(len(G[0])):
            if G[y][x] == 'S':
                S = (x, y)

    splits = 0
    beams = set([S])
    visited = set()
    while len(beams) > 0:
        x, y = beams.pop()
        if (x, y) in visited:
            continue

        if 0 <= x < len(G[0]) and 0 <= y < len(G):
            visited.add((x, y))
            if y == len(G)-1:
                continue

            if G[y+1][x] == '^':
                splits += 1
                beams.add((x-1,y+1))
                beams.add((x+1,y+1))
            else:
                beams.add((x, y+1))

    print(splits)


def p2():
    D = open(f'{sys.argv[1]}.txt').read().strip().split('\n\n')
    G = [list(row) for row in D[0].split('\n')]
    S = (0, 0)

    for y in range(len(G)):
        for x in range(len(G[0])):
            if G[y][x] == 'S':
                S = (x, y)

    current = { S[0]: 1 }
    for row in range(len(G)):
        next = {}
        for col, count in current.items():
            if col < 0 or col >= len(G[0]):
                continue

            if G[row][col] == '^':
                next[col-1] = next.get(col-1, 0) + count
                next[col+1] = next.get(col+1, 0) + count
            else:
                next[col] = next.get(col, 0) + count
        current = next


    print(sum(current.values()))


p1()
p2()