import re

def part_1(input):
    return sum(int(a) <= pw.count(char) <= int(b) for a,b,char,pw in input)

def part_2(input):
    return sum((pw[int(a)-1] == char) != (pw[int(b)-1] == char) for a,b,char,pw in input)

with open("2020/Day02_input.txt") as f:
    input = [re.split("-| |: ", line.strip()) for line in f]

    print(f"Part 1: {part_1(input)}")
    print(f"Part 2: {part_2(input)}")
