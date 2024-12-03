import re

def part_1(memory):
    return sum(int(a)*int(b) for a,b in re.findall(r'mul\((\d+),(\d+)\)', memory))

def part_2(memory):
    total, enabled = 0, True
    for m in re.finditer(r"mul\((\d+),(\d+)\)|do\(\)|don't\(\)", memory):
        if m[0] == 'do()':
            enabled = True
        elif m[0] == "don't()":
            enabled = False
        elif enabled:
            total += int(m[1]) * int(m[2])
    return total

with open("2024/Day03_input.txt") as f:
    memory = f.read()

    print(f"Part 1: {part_1(memory)}")
    print(f"Part 2: {part_2(memory)}")
