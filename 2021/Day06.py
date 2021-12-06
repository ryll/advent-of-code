def simulate(input, days):
    counts = [input.count(i) for i in range(9)]
    for _ in range(days):
        counts = counts[1:] + counts[:1]
        counts[6] += counts[8]
    return sum(counts)

def part_1(input):
    return simulate(input, 80)

def part_2(input):
    return simulate(input, 256)

with open("2021/Day06_input.txt") as f:
    input = [int(x) for x in f.read().split(',')]

    print(f"Part 1: {part_1(input)}")
    print(f"Part 2: {part_2(input)}")
