import re
from collections import Counter

def claimed(input):
    return Counter((x,y) for _,l,t,w,h in input
                   for x in range(l, l+w) for y in range(t, t+h))

def part_1(input):
    return sum(n > 1 for n in claimed(input).values())

def part_2(input):
    counts = claimed(input)
    for id,l,t,w,h in input:
        if all(counts[(x,y)] == 1 for x in range(l, l+w) for y in range(t, t+h)):
            return id

with open("2018/Day03_input.txt") as f:
    input = [tuple(int(v) for v in re.findall(r'\d+', line)) for line in f.read().splitlines()]

    print(f"Part 1: {part_1(input)}")
    print(f"Part 2: {part_2(input)}")
