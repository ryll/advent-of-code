from itertools import permutations

def part_1(input):
    return sum(max(row) - min(row) for row in input)

def part_2(input):
    return sum(a // b for row in input for a,b in permutations(row, 2) if a % b == 0)

with open("2017/Day02_input.txt") as f:
    input = [[int(v) for v in line.split()] for line in f.read().splitlines() if line]

    print(f"Part 1: {part_1(input)}")
    print(f"Part 2: {part_2(input)}")
