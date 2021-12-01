def part_1(input):
    return sum(b > a for a,b in zip(input, input[1:]))

def part_2(input):
    return sum(b > a for a,b in zip(input, input[3:]))

with open("2021/Day01_input.txt") as f:
    input = [int(x) for x in f.read().split()]

    print(f"Part 1: {part_1(input)}")
    print(f"Part 2: {part_2(input)}")
