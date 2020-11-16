import operator
from collections import defaultdict

COMPARISONS = {'>': operator.gt, '<': operator.lt, '>=': operator.ge,
               '<=': operator.le, '==': operator.eq, '!=': operator.ne}

def run(input):
    registers, highest = defaultdict(int), 0
    for target, op, amount, check, comparison, value in input:
        if COMPARISONS[comparison](registers[check], value):
            registers[target] += amount if op == 'inc' else -amount
            highest = max(highest, registers[target])
    return max(registers.values()), highest

def part_1(input):
    return run(input)[0]

def part_2(input):
    return run(input)[1]

with open("2017/Day08_input.txt") as f:
    input = [(target, op, int(amount), check, comparison, int(value))
             for target, op, amount, _, check, comparison, value
             in (line.split() for line in f.read().splitlines() if line)]

    print(f"Part 1: {part_1(input)}")
    print(f"Part 2: {part_2(input)}")
