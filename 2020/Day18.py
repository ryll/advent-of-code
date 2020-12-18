import re

def calculate(expression, addition_first):
    while '(' in expression:
        expression = re.sub(r"\(([^()]*)\)", lambda m: str(calculate(m[1], addition_first)), expression)
    if addition_first:
        while '+' in expression:
            expression = re.sub(r"(\d+) \+ (\d+)", lambda m: str(int(m[1]) + int(m[2])), expression, count=1)
    while ' ' in expression:
        expression = re.sub(r"(\d+) ([+*]) (\d+)",
                            lambda m: str(int(m[1]) + int(m[3]) if m[2] == '+' else int(m[1]) * int(m[3])),
                            expression, count=1)
    return int(expression)

def part_1(input):
    return sum(calculate(line, False) for line in input)

def part_2(input):
    return sum(calculate(line, True) for line in input)

with open("2020/Day18_input.txt") as f:
    input = f.read().splitlines()

    print(f"Part 1: {part_1(input)}")
    print(f"Part 2: {part_2(input)}")
