import re

def part_1(input):
    limits = {'red':12, 'green':13, 'blue':14}
    return sum(i for i,game in enumerate(input, 1) if all(n <= limits[c] for n,c in game))

def part_2(input):
    total = 0
    for game in input:
        power = 1
        for colour in ('red', 'green', 'blue'):
            power *= max(n for n,c in game if c == colour)
        total += power
    return total

with open("2023/Day02_input.txt") as f:
    input = [[(int(n), c) for n,c in re.findall(r"(\d+) (\w+)", line.split(': ')[1])]
             for line in f.read().splitlines()]

    print(f"Part 1: {part_1(input)}")
    print(f"Part 2: {part_2(input)}")
