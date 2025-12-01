import sys
from collections import deque

D = open(f'{sys.argv[1]}.txt').read().strip().split('\n')
grid = [list(line) for line in D]
rows = len(grid)
cols = len(grid[0])

start = (0, 0)
end = (0, 0)
count = 0

for r in range(rows):
  for c in range(cols):
    if grid[r][c] == 'S':
      start = (r, c)
    if grid[r][c] == 'E':
      end = (r, c)
    if grid[r][c] == '.':
      count += 1

print(count)
print(start, end)
path = [start]
found = False

while not found:
  r, c = path[-1]
  neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]
  neighbors = [(r + rr, c + cc) for rr, cc in neighbors]

  for n in neighbors:
    rr, cc = n
    if rr < 0 or rr >= rows or cc < 0 or cc >= cols:
      continue
    if grid[rr][cc] == '#':
      continue

    if n not in path:
      if n == end:
        found = True
        break
      path.append(n)

print(len(path))



