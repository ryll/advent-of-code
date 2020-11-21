from itertools import count

def drop(discs):
    return next(t for t in count()
                if all((start + t + i + 1) % positions == 0
                       for i,(positions,start) in enumerate(discs)))

def part_1(discs):
    return drop(discs)

def part_2(discs):
    return drop(discs + [(11, 0)])

with open("2016/Day15_input.txt") as f:
    discs = [(int(line.split()[3]), int(line.split()[11][:-1])) for line in f.read().splitlines()]

    print(f"Part 1: {part_1(discs)}")
    print(f"Part 2: {part_2(discs)}")
