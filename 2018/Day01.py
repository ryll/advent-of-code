from itertools import accumulate, cycle

def part_1(input):
    return sum(input)

def part_2(input):
    seen = {0}
    for frequency in accumulate(cycle(input)):
        if frequency in seen:
            return frequency
        seen.add(frequency)

with open("2018/Day01_input.txt") as f:
    input = [int(x) for x in f.read().split()]

    print(f"Part 1: {part_1(input)}")
    print(f"Part 2: {part_2(input)}")
