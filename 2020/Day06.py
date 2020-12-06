def part_1(input):
    return sum(len(set.union(*group)) for group in input)

def part_2(input):
    return sum(len(set.intersection(*group)) for group in input)

with open("2020/Day06_input.txt") as f:
    input = [[set(line) for line in block.split()] for block in f.read().split("\n\n")]

    print(f"Part 1: {part_1(input)}")
    print(f"Part 2: {part_2(input)}")
