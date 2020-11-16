from collections import defaultdict

def value(registers, x):
    return registers[x] if x.isalpha() else int(x)

def part_1(input):
    registers, i, muls = defaultdict(int), 0, 0
    while 0 <= i < len(input):
        op, x, y = input[i]
        if op == 'set':   registers[x] = value(registers, y)
        elif op == 'sub': registers[x] -= value(registers, y)
        elif op == 'mul':
            registers[x] *= value(registers, y)
            muls += 1
        elif op == 'jnz' and value(registers, x) != 0:
            i += value(registers, y) - 1
        i += 1
    return muls

def part_2(input):
    b = int(input[0][2]) * 100 + 100000
    return sum(any(n % d == 0 for d in range(2, int(n**0.5) + 1))
               for n in range(b, b + 17001, 17))

with open("2017/Day23_input.txt") as f:
    input = [line.split() for line in f.read().splitlines() if line]

    print(f"Part 1: {part_1(input)}")
    print(f"Part 2: {part_2(input)}")
