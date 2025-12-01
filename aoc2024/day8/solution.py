import sys
import math
from collections import defaultdict
import operator

def p1():
  grid = [list(row) for row in open(f'{sys.argv[1]}.txt').read().strip().split('\n')]
  rows = len(grid)
  cols = len(grid[0])

  antennas = defaultdict(list)

  for r in range(rows):
    for c in range(cols):
      if grid[r][c] == '.':
        continue

      a = grid[r][c]
      antennas[a].append((r, c))

  nodes = set()
  for antenna in antennas:
    for i in range(len(antennas[antenna])):
      for j in range(i + 1, len(antennas[antenna])):
        r1, c1 = antennas[antenna][i]
        r2, c2 = antennas[antenna][j]
        dr, dc = r1 - r2, c1 - c2
        nodes.add((r1 + dr, c1 + dc))
        nodes.add((r2 - dr, c2 - dc))

  count = 0
  for node in nodes:
    nr, nc = node
    if nr >= 0 and nr < rows and nc >= 0 and nc < cols:
      count += 1

  print(count)


def p2():
  grid = [list(row) for row in open(f'{sys.argv[1]}.txt').read().strip().split('\n')]
  rows = len(grid)
  cols = len(grid[0])

  def get_nodes(r, c, dr, dc, op):
    nodes = set()
    while r >= 0 and r < rows and c >= 0 and c < cols:
      nodes.add((r, c))
      r = op(r, dr)
      c = op(c, dc)
    return nodes

  antennas = defaultdict(list)
  for r in range(rows):
    for c in range(cols):
      if grid[r][c] == '.':
        continue

      a = grid[r][c]
      antennas[a].append((r, c))

  nodes = set()
  for antenna in antennas:
    for i in range(len(antennas[antenna])):
      for j in range(i + 1, len(antennas[antenna])):
        r1, c1 = antennas[antenna][i]
        r2, c2 = antennas[antenna][j]
        dr, dc = r1 - r2, c1 - c2

        # print(r1, c1)
        # print(r2, c2)
        # print(get_nodes(r1, c1, dr, dc, operator.add))
        # print(get_nodes(r2, c2, dr, dc, operator.sub))
        # print('----')
        nodes = nodes.union(get_nodes(r1, c1, dr, dc, operator.add))
        nodes = nodes.union(get_nodes(r2, c2, dr, dc, operator.sub))

  print(len(nodes))


print('Part 1:')
p1()
print('Part 2:')
p2()