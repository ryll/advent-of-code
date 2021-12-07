def part_1(input):
    return min(sum(abs(c-p) for c in input) for p in range(min(input), max(input)+1))

def part_2(input):
    return min(sum(abs(c-p)*(abs(c-p)+1)//2 for c in input) for p in range(min(input), max(input)+1))

with open("2021/Day07_input.txt") as f:
    input = [int(x) for x in f.read().split(',')]

    print(f"Part 1: {part_1(input)}")
    print(f"Part 2: {part_2(input)}")
