def part_1(input):
    return sum(len(s) - len(eval(s)) for s in input)

def part_2(input):
    return sum(2 + s.count('"') + s.count('\\') for s in input)

with open("2015/Day08_input.txt") as f:
    input = f.read().split()

    print(f"Part 1: {part_1(input)}")
    print(f"Part 2: {part_2(input)}")
