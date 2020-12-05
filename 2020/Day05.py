def part_1(input):
    return max(input)

def part_2(input):
    return next(i for i in range(min(input), max(input)) if i not in input and i-1 in input and i+1 in input)

with open("2020/Day05_input.txt") as f:
    input = {int(line.strip().translate(str.maketrans("FBLR", "0101")), 2) for line in f}

    print(f"Part 1: {part_1(input)}")
    print(f"Part 2: {part_2(input)}")
