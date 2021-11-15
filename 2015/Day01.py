def part_1(input):
    return input.count('(') - input.count(')')

def part_2(input):
    floor = 0
    for i,c in enumerate(input, 1):
        floor += 1 if c == '(' else -1
        if floor < 0:
            return i

with open("2015/Day01_input.txt") as f:
    input = f.read().strip()

    print(f"Part 1: {part_1(input)}")
    print(f"Part 2: {part_2(input)}")
