from collections import Counter

def part_1(left, right):
    return sum(abs(a-b) for a,b in zip(sorted(left), sorted(right)))

def part_2(left, right):
    counts = Counter(right)
    return sum(a * counts[a] for a in left)

with open("2024/Day01_input.txt") as f:
    left, right = zip(*(tuple(int(v) for v in line.split()) for line in f.read().splitlines()))

    print(f"Part 1: {part_1(left, right)}")
    print(f"Part 2: {part_2(left, right)}")
