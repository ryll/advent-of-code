from itertools import groupby

def look_and_say(input, rounds):
    for _ in range(rounds):
        input = ''.join(f"{len(list(run))}{digit}" for digit,run in groupby(input))
    return len(input)

def part_1(input):
    return look_and_say(input, 40)

def part_2(input):
    return look_and_say(input, 50)

with open("2015/Day10_input.txt") as f:
    input = f.read().strip()

    print(f"Part 1: {part_1(input)}")
    print(f"Part 2: {part_2(input)}")
