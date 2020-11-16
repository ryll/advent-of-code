from functools import reduce
from operator import xor

def knot(lengths):
    numbers, pos, skip = list(range(256)), 0, 0
    for _ in range(64):
        for length in lengths:
            for i in range(length // 2):
                a, b = (pos+i) % 256, (pos+length-1-i) % 256
                numbers[a], numbers[b] = numbers[b], numbers[a]
            pos = (pos + length + skip) % 256
            skip += 1
    return [reduce(xor, numbers[i:i+16]) for i in range(0, 256, 16)]

def grid(key):
    used = set()
    for row in range(128):
        digest = knot([ord(c) for c in f"{key}-{row}"] + [17, 31, 73, 47, 23])
        bits = ''.join(f"{b:08b}" for b in digest)
        used |= {(row, col) for col,bit in enumerate(bits) if bit == '1'}
    return used

def part_1(input):
    return len(grid(input))

def part_2(input):
    used, regions = grid(input), 0
    while used:
        stack = [used.pop()]
        while stack:
            row, col = stack.pop()
            for n in ((row-1,col), (row+1,col), (row,col-1), (row,col+1)):
                if n in used:
                    used.remove(n)
                    stack.append(n)
        regions += 1
    return regions

with open("2017/Day14_input.txt") as f:
    input = f.read().strip()

    print(f"Part 1: {part_1(input)}")
    print(f"Part 2: {part_2(input)}")
