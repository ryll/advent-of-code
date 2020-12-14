from itertools import product

def part_1(input):
    mem, mask = {}, '0'*36
    for target,value in input:
        if target == 'mask':
            mask = value
        else:
            bits = f"{int(value):036b}"
            mem[target] = int(''.join(b if m == 'X' else m for m,b in zip(mask, bits)), 2)
    return sum(mem.values())

def part_2(input):
    mem, mask = {}, '0'*36
    for target,value in input:
        if target == 'mask':
            mask = value
            continue
        bits = f"{int(target):036b}"
        floating = ''.join(b if m == '0' else m for m,b in zip(mask, bits))
        for fill in product('01', repeat=floating.count('X')):
            fill = iter(fill)
            mem[''.join(next(fill) if c == 'X' else c for c in floating)] = int(value)
    return sum(mem.values())

with open("2020/Day14_input.txt") as f:
    input = [(left.strip().removeprefix('mem[').removesuffix(']'), right.strip())
             for left,right in (line.split('=') for line in f)]

    print(f"Part 1: {part_1(input)}")
    print(f"Part 2: {part_2(input)}")
