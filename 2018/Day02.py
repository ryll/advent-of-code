from collections import Counter

def part_1(input):
    counts = [set(Counter(box).values()) for box in input]
    return sum(2 in c for c in counts) * sum(3 in c for c in counts)

def part_2(input):
    for i,a in enumerate(input):
        for b in input[i+1:]:
            if len(common := [x for x,y in zip(a,b) if x == y]) == len(a) - 1:
                return ''.join(common)

with open("2018/Day02_input.txt") as f:
    input = f.read().split()

    print(f"Part 1: {part_1(input)}")
    print(f"Part 2: {part_2(input)}")
