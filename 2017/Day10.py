from functools import reduce
from operator import xor

def knot(lengths, rounds):
    numbers, pos, skip = list(range(256)), 0, 0
    for _ in range(rounds):
        for length in lengths:
            for i in range(length // 2):
                a, b = (pos+i) % 256, (pos+length-1-i) % 256
                numbers[a], numbers[b] = numbers[b], numbers[a]
            pos = (pos + length + skip) % 256
            skip += 1
    return numbers

def part_1(input):
    numbers = knot([int(v) for v in input.split(',')], 1)
    return numbers[0] * numbers[1]

def part_2(input):
    numbers = knot([ord(c) for c in input] + [17, 31, 73, 47, 23], 64)
    return ''.join(f"{reduce(xor, numbers[i:i+16]):02x}" for i in range(0, 256, 16))

with open("2017/Day10_input.txt") as f:
    input = f.read().strip()

    print(f"Part 1: {part_1(input)}")
    print(f"Part 2: {part_2(input)}")
