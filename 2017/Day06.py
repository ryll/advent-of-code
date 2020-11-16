def redistribute(input):
    banks, seen = list(input), {}
    while tuple(banks) not in seen:
        seen[tuple(banks)] = len(seen)
        i = banks.index(max(banks))
        blocks, banks[i] = banks[i], 0
        for j in range(1, blocks + 1):
            banks[(i+j) % len(banks)] += 1
    return len(seen), len(seen) - seen[tuple(banks)]

def part_1(input):
    return redistribute(input)[0]

def part_2(input):
    return redistribute(input)[1]

with open("2017/Day06_input.txt") as f:
    input = [int(v) for v in f.read().split()]

    print(f"Part 1: {part_1(input)}")
    print(f"Part 2: {part_2(input)}")
