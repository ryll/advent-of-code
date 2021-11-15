from hashlib import md5
from itertools import count

def mine(key, zeroes):
    return next(i for i in count(1) if md5(f"{key}{i}".encode()).hexdigest().startswith('0' * zeroes))

def part_1(input):
    return mine(input, 5)

def part_2(input):
    return mine(input, 6)

with open("2015/Day04_input.txt") as f:
    input = f.read().strip()

    print(f"Part 1: {part_1(input)}")
    print(f"Part 2: {part_2(input)}")
