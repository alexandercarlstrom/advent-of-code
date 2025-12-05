import sys
import re
import math
from itertools import accumulate as acc
from itertools import chain as flatten


def p1():
    D = open(f'{sys.argv[1]}.txt').read().strip().split('\n\n')
    G = D[0].split('\n')
    count = 0
    for y in range(len(G)):
        for x in range(len(G[y])):
            if (G[y][x] == '@'):
                adjacent = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
                count_adjacent = 0
                for dx, dy in adjacent:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < len(G[y]) and 0 <= ny < len(G):
                        if G[ny][nx] == '@':
                            count_adjacent += 1

                if count_adjacent < 4:
                    count += 1
    print(count)

def get_one_dim_index(x, y, width):
    return y * width + x

def p2():
    D = open(f'{sys.argv[1]}.txt').read().strip().split('\n\n')
    G = [list(line) for line in D[0].split('\n')]

    count = 0
    while True:
        removed = set()
        for y in range(len(G)):
            for x in range(len(G[y])):
                if (G[y][x] == '@'):
                    adjacent = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
                    count_adjacent = 0
                    for dx, dy in adjacent:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < len(G[y]) and 0 <= ny < len(G):
                            if G[ny][nx] == '@':
                                count_adjacent += 1

                    if count_adjacent < 4:
                        removed.add((x, y))

        if len(removed) == 0:
            break

        for x, y in removed:
            G[y][x] = 'x'

        count += len(removed)
    print(count)


p2()