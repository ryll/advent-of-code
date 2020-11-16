from itertools import count

def caught(input, delay):
    return [(depth, r) for depth,r in input if (depth + delay) % (2*(r-1)) == 0]

def part_1(input):
    return sum(depth * r for depth,r in caught(input, 0))

def part_2(input):
    return next(delay for delay in count()
                if not any((depth + delay) % (2*(r-1)) == 0 for depth,r in input))

with open("2017/Day13_input.txt") as f:
    input = [tuple(int(v) for v in line.split(': ')) for line in f.read().splitlines() if line]

    print(f"Part 1: {part_1(input)}")
    print(f"Part 2: {part_2(input)}")
