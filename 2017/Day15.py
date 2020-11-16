import re

def generate(value, factor, multiple):
    while True:
        value = value * factor % 2147483647
        if value % multiple == 0:
            yield value

def judge(start_a, start_b, pairs, multiple_a, multiple_b):
    a, b = generate(start_a, 16807, multiple_a), generate(start_b, 48271, multiple_b)
    return sum(next(a) & 0xffff == next(b) & 0xffff for _ in range(pairs))

def part_1(a, b):
    return judge(a, b, 40000000, 1, 1)

def part_2(a, b):
    return judge(a, b, 5000000, 4, 8)

with open("2017/Day15_input.txt") as f:
    a, b = (int(v) for v in re.findall(r'\d+', f.read()))

    print(f"Part 1: {part_1(a, b)}")
    print(f"Part 2: {part_2(a, b)}")
