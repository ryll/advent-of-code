from collections import Counter

def part_1(lines):
    return ''.join(Counter(column).most_common()[0][0] for column in zip(*lines))

def part_2(lines):
    return ''.join(Counter(column).most_common()[-1][0] for column in zip(*lines))

with open("2016/Day06_input.txt") as f:
    lines = f.read().split()

    print(f"Part 1: {part_1(lines)}")
    print(f"Part 2: {part_2(lines)}")
