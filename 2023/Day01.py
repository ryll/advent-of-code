import re

DIGITS = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5,
          'six':6, 'seven':7, 'eight':8, 'nine':9}

def calibration(input, pattern):
    total = 0
    for line in input:
        found = [int(m) if m.isdigit() else DIGITS[m] for m in re.findall(pattern, line)]
        total += 10*found[0] + found[-1]
    return total

def part_1(input):
    return calibration(input, r"(?=(\d))")

def part_2(input):
    return calibration(input, r"(?=(\d|" + '|'.join(DIGITS) + r"))")

with open("2023/Day01_input.txt") as f:
    input = f.read().split()

    print(f"Part 1: {part_1(input)}")
    print(f"Part 2: {part_2(input)}")
