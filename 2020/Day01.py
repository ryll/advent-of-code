def part_1(input):
    return next(i*(2020-i) for i in input if 2020-i in input)

def part_2(input):
    return next(i*j*(2020-i-j) for i in input for j in input if 2020-i-j in input)

with open("2020/Day01_input.txt") as f:
    input = set(map(int, f.read().split()))

    print(f"Part 1: {part_1(input)}")
    print(f"Part 2: {part_2(input)}")
