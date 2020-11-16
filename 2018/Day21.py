OPS = {
    'addr': lambda r,a,b: r[a] + r[b],   'addi': lambda r,a,b: r[a] + b,
    'mulr': lambda r,a,b: r[a] * r[b],   'muli': lambda r,a,b: r[a] * b,
    'banr': lambda r,a,b: r[a] & r[b],   'bani': lambda r,a,b: r[a] & b,
    'borr': lambda r,a,b: r[a] | r[b],   'bori': lambda r,a,b: r[a] | b,
    'setr': lambda r,a,b: r[a],          'seti': lambda r,a,b: a,
    'gtir': lambda r,a,b: int(a > r[b]), 'gtri': lambda r,a,b: int(r[a] > b),
    'gtrr': lambda r,a,b: int(r[a] > r[b]),
    'eqir': lambda r,a,b: int(a == r[b]), 'eqri': lambda r,a,b: int(r[a] == b),
    'eqrr': lambda r,a,b: int(r[a] == r[b]),
}

def halting(program, pointer):
    check = next(i for i,(name,*_) in enumerate(program) if name == 'eqrr')
    compared = program[check][1] if program[check][2] == 0 else program[check][2]
    registers, seen, first, last = [0] * 6, set(), None, None
    while 0 <= registers[pointer] < len(program):
        if registers[pointer] == check:
            value = registers[compared]
            if value in seen:
                return first, last
            first = value if first is None else first
            last = value
            seen.add(value)
        name, a, b, c = program[registers[pointer]]
        registers[c] = OPS[name](registers, a, b)
        registers[pointer] += 1
    return first, last

def part_1(program, pointer):
    return halting(program, pointer)[0]

def part_2(program, pointer):
    return halting(program, pointer)[1]

with open("2018/Day21_input.txt") as f:
    header, *lines = f.read().splitlines()
    pointer = int(header.split()[1])
    program = [(name, *(int(v) for v in args))
               for name,*args in (line.split() for line in lines if line)]

    print(f"Part 1: {part_1(program, pointer)}")
    print(f"Part 2: {part_2(program, pointer)}")
