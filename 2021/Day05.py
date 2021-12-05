from collections import Counter

def sign(n):
    return (n > 0) - (n < 0)

def overlaps(input, diagonals):
    counts = Counter()
    for x1,y1,x2,y2 in input:
        dx, dy = sign(x2-x1), sign(y2-y1)
        if dx and dy and not diagonals:
            continue
        for i in range(max(abs(x2-x1), abs(y2-y1)) + 1):
            counts[x1+dx*i, y1+dy*i] += 1
    return sum(n > 1 for n in counts.values())

def part_1(input):
    return overlaps(input, False)

def part_2(input):
    return overlaps(input, True)

with open("2021/Day05_input.txt") as f:
    input = [[int(v) for v in line.replace(' -> ', ',').split(',')] for line in f.read().splitlines()]

    print(f"Part 1: {part_1(input)}")
    print(f"Part 2: {part_2(input)}")
