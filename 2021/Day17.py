import re

def hits(input, vx, vy):
    x1, x2, y1, y2 = input
    x = y = 0
    while x <= x2 and y >= y1:
        if x >= x1 and y <= y2:
            return True
        x, y, vx, vy = x+vx, y+vy, max(vx-1, 0), vy-1
    return False

def part_1(input):
    return input[2] * (input[2]+1) // 2

def part_2(input):
    return sum(hits(input, vx, vy) for vx in range(input[1]+1)
               for vy in range(input[2], -input[2]+1))

with open("2021/Day17_input.txt") as f:
    input = [int(v) for v in re.findall(r"-?\d+", f.read())]

    print(f"Part 1: {part_1(input)}")
    print(f"Part 2: {part_2(input)}")
