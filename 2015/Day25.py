import re

def part_1(row, col):
    n = (row + col - 2) * (row + col - 1) // 2 + col
    return 20151125 * pow(252533, n - 1, 33554393) % 33554393

def part_2(row, col):
    return "Merry Christmas!"

with open("2015/Day25_input.txt") as f:
    row, col = (int(x) for x in re.findall(r'\d+', f.read()))

    print(f"Part 1: {part_1(row, col)}")
    print(f"Part 2: {part_2(row, col)}")
