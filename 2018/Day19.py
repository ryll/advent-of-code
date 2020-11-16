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

def run(program, pointer, registers, steps=None):
    while 0 <= registers[pointer] < len(program) and steps != 0:
        name, a, b, c = program[registers[pointer]]
        registers[c] = OPS[name](registers, a, b)
        registers[pointer] += 1
        if steps is not None:
            steps -= 1
    return registers

def part_1(program, pointer):
    return run(program, pointer, [0] * 6)[0]

def part_2(program, pointer):
    n = max(run(program, pointer, [1, 0, 0, 0, 0, 0], 1000))
    return sum({d for i in range(1, int(n**0.5) + 1) if n % i == 0 for d in (i, n//i)})

with open("2018/Day19_input.txt") as f:
    header, *lines = f.read().splitlines()
    pointer = int(header.split()[1])
    program = [(name, *(int(v) for v in args))
               for name,*args in (line.split() for line in lines if line)]

    print(f"Part 1: {part_1(program, pointer)}")
    print(f"Part 2: {part_2(program, pointer)}")
