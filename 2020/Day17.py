from collections import Counter
from itertools import product

def run(active, dims):
    active = {cell + (0,)*(dims-2) for cell in active}
    for _ in range(6):
        counts = Counter(tuple(c+d for c,d in zip(cell, delta))
                         for cell in active
                         for delta in product((-1,0,1), repeat=dims) if any(delta))
        active = {cell for cell,n in counts.items() if n == 3 or (n == 2 and cell in active)}
    return len(active)

def part_1(input):
    return run(input, 3)

def part_2(input):
    return run(input, 4)

with open("2020/Day17_input.txt") as f:
    input = {(i,j) for i,row in enumerate(f.read().split()) for j,c in enumerate(row) if c == '#'}

    print(f"Part 1: {part_1(input)}")
    print(f"Part 2: {part_2(input)}")
