def loop_size(key):
    value, loops = 1, 0
    while value != key:
        value, loops = value * 7 % 20201227, loops + 1
    return loops

def part_1(input):
    return pow(input[0], loop_size(input[1]), 20201227)

def part_2(input):
    return "Merry Christmas!"

with open("2020/Day25_input.txt") as f:
    input = [int(x) for x in f.read().split()]

    print(f"Part 1: {part_1(input)}")
    print(f"Part 2: {part_2(input)}")
