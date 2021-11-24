from itertools import combinations

def fits(input, litres=150):
    return [n for n in range(1, len(input) + 1)
            for combo in combinations(input, n) if sum(combo) == litres]

def part_1(input):
    return len(fits(input))

def part_2(input):
    counts = fits(input)
    return counts.count(min(counts))

with open("2015/Day17_input.txt") as f:
    input = [int(x) for x in f.read().split()]

    print(f"Part 1: {part_1(input)}")
    print(f"Part 2: {part_2(input)}")
