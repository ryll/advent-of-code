def run(program, registers):
    def value(a):
        return registers[a] if a in registers else int(a)
    ip = 0
    while 0 <= ip < len(program):
        op, *args = program[ip]
        if op == 'cpy':
            registers[args[1]] = value(args[0])
        elif op == 'inc':
            registers[args[0]] += 1
        elif op == 'dec':
            registers[args[0]] -= 1
        elif op == 'jnz' and value(args[0]):
            ip += value(args[1]) - 1
        ip += 1
    return registers['a']

def part_1(program):
    return run(program, dict.fromkeys('abcd', 0))

def part_2(program):
    return run(program, dict.fromkeys('abcd', 0) | {'c': 1})

with open("2016/Day12_input.txt") as f:
    program = [line.split() for line in f.read().splitlines()]

    print(f"Part 1: {part_1(program)}")
    print(f"Part 2: {part_2(program)}")
