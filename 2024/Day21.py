from functools import cache
from itertools import permutations

NUMPAD = {'7': (0,0), '8': (0,1), '9': (0,2), '4': (1,0), '5': (1,1), '6': (1,2),
          '1': (2,0), '2': (2,1), '3': (2,2), '0': (3,1), 'A': (3,2)}
DIRPAD = {'^': (0,1), 'A': (0,2), '<': (1,0), 'v': (1,1), '>': (1,2)}
STEPS = {'^': (-1,0), 'v': (1,0), '<': (0,-1), '>': (0,1)}

@cache
def routes(a, b, numeric):
    pad, gap = (NUMPAD, (3,0)) if numeric else (DIRPAD, (0,0))
    (i1,j1), (i2,j2) = pad[a], pad[b]
    moves = '^' * (i1-i2) + 'v' * (i2-i1) + '<' * (j1-j2) + '>' * (j2-j1)
    found = set()
    for candidate in set(permutations(moves)):
        i, j = i1, j1
        for move in candidate:
            di, dj = STEPS[move]
            i, j = i+di, j+dj
            if (i,j) == gap:
                break
        else:
            found.add(''.join(candidate) + 'A')
    return tuple(found)

@cache
def presses(sequence, depth, numeric=False):
    if depth == 0:
        return len(sequence)
    total, previous = 0, 'A'
    for button in sequence:
        total += min(presses(r, depth-1) for r in routes(previous, button, numeric))
        previous = button
    return total

def complexity(codes, robots):
    return sum(presses(code, robots+1, True) * int(code[:-1]) for code in codes)

def part_1(codes):
    return complexity(codes, 2)

def part_2(codes):
    return complexity(codes, 25)

with open("2024/Day21_input.txt") as f:
    codes = f.read().split()

    print(f"Part 1: {part_1(codes)}")
    print(f"Part 2: {part_2(codes)}")
