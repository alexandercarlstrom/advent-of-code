import sys
import re

def p1():
  D = open(f'{sys.argv[1]}.txt').read().strip().split('\n\n')
  gates = dict()

  for line in D[0].split('\n'):
    search = re.search(r'(\S+): (\d+)', line)
    name, num = search.groups()
    gates[name] = num

  predefined = len(gates.values())
  instructions = []

  for line in D[1].split('\n'):
    search = re.search(r'(\S+) (AND|OR|XOR) (\S+) -> (\S+)', line)
    first, condition, second, target = search.groups()
    instructions.append((first, condition, second, target))

  while len(instructions) != 0:
    first, condition, second, target = instructions.pop(0)
    if first not in gates or second not in gates:
      instructions.append((first, condition, second, target))
      continue

    if condition == 'AND':
      gates[target] = '1' if gates[first] == gates[second] and gates[first] == '1' else '0'
    if condition == 'OR':
      gates[target] = '1' if gates[first] == '1' or gates[second] == '1' else '0'
    if condition == 'XOR':
      gates[target] = '1' if gates[first] != gates[second] else '0'

  keys = list(gates.keys())[predefined:]
  keys.sort()

  binary = ''
  for key in keys:
    if key.startswith('z'):
      binary += gates[key]

  print(binary[::-1])
  print('Part 1:', int(binary[::-1], 2))
  print(int('101010', 2), int('101100', 2))
  print(int('101010', 2) + int('101100', 2))
  print(format(int('101010', 2) + int('101100', 2), 'b'))


def p2():
  D = open(f'{sys.argv[1]}.txt').read().strip().split('\n\n')
  formulas = dict()

  for line in D[1].split('\n'):
    x, op, y, z = line.replace(' -> ', ' ').split(' ')
    formulas[z] = (op, x, y)

  def pp(wire, depth=0):
    if wire[0] in 'xy':
      return '  ' * depth + wire
    op, x, y = formulas[wire]
    return '  ' * depth + op  + f' ({wire})\n{pp(x, depth + 1)}\n{pp(y, depth + 1)}'

  print(pp('z02'))

p2()
# binary = ''.join(list(list(gates.values())[predefined:].sort()))[::-1]