def part_1(ranges):
    lowest = 0
    for low,high in sorted(ranges):
        if low > lowest:
            break
        lowest = max(lowest, high + 1)
    return lowest

def part_2(ranges):
    allowed, lowest = 0, 0
    for low,high in sorted(ranges):
        allowed += max(0, low - lowest)
        lowest = max(lowest, high + 1)
    return allowed + 2**32 - lowest

with open("2016/Day20_input.txt") as f:
    ranges = [tuple(int(v) for v in line.split('-')) for line in f.read().split()]

    print(f"Part 1: {part_1(ranges)}")
    print(f"Part 2: {part_2(ranges)}")
