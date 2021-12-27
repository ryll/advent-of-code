from functools import cache

def run(block, digit, z):
    target, instructions = block
    registers = {'w':0, 'x':0, 'y':0, 'z':z, target:digit}
    for op,*args in instructions:
        a = args[0]
        b = registers[args[1]] if args[1] in registers else int(args[1])
        if op == 'add':   registers[a] += b
        elif op == 'mul': registers[a] *= b
        elif op == 'div': registers[a] = int(registers[a] / b)
        elif op == 'mod': registers[a] %= b
        elif op == 'eql': registers[a] = int(registers[a] == b)
    return registers['z']

def search(blocks, digits):
    @cache
    def best(i, z):
        if i == len(blocks):
            return '' if z == 0 else None
        for d in digits:
            if (rest := best(i+1, run(blocks[i], d, z))) is not None:
                return str(d) + rest
        return None
    return best(0, 0)

def part_1(input):
    return search(input, (9,8,7,6,5,4,3,2,1))

def part_2(input):
    return search(input, (1,2,3,4,5,6,7,8,9))

with open("2021/Day24_input.txt") as f:
    input = []
    for line in f.read().splitlines():
        op, *args = line.split()
        if op == 'inp':
            input.append((args[0], []))
        else:
            input[-1][1].append((op, *args))

    print(f"Part 1: {part_1(input)}")
    print(f"Part 2: {part_2(input)}")
