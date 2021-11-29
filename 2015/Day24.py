from itertools import combinations
from math import prod

def best(input, groups):
    target = sum(input) // groups
    for n in range(1, len(input) + 1):
        entanglements = [prod(combo) for combo in combinations(input, n) if sum(combo) == target]
        if entanglements:
            return min(entanglements)

def part_1(input):
    return best(input, 3)

def part_2(input):
    return best(input, 4)

with open("2015/Day24_input.txt") as f:
    input = [int(x) for x in f.read().split()]

    print(f"Part 1: {part_1(input)}")
    print(f"Part 2: {part_2(input)}")
