def deliver(target, per_elf, limit=None):
    size = target // per_elf + 1
    houses = [0] * size
    for elf in range(1, size):
        stop = size if limit is None else min(size, elf * limit + 1)
        for house in range(elf, stop, elf):
            houses[house] += elf * per_elf
    return next(i for i,presents in enumerate(houses) if presents >= target)

def part_1(input):
    return deliver(input, 10)

def part_2(input):
    return deliver(input, 11, 50)

with open("2015/Day20_input.txt") as f:
    input = int(f.read().strip())

    print(f"Part 1: {part_1(input)}")
    print(f"Part 2: {part_2(input)}")
