from itertools import count, islice

def run(program, a):
    registers = dict.fromkeys('abcd', 0) | {'a': a}
    def value(x):
        return registers[x] if x in registers else int(x)
    ip = 0
    while 0 <= ip < len(program):
        op, *args = program[ip]
        if op == 'cpy':
            registers[args[1]] = value(args[0])
        elif op == 'inc':
            registers[args[0]] += 1
        elif op == 'dec':
            registers[args[0]] -= 1
        elif op == 'out':
            yield value(args[0])
        elif op == 'jnz' and value(args[0]):
            ip += value(args[1]) - 1
        ip += 1

def part_1(program):
    return next(a for a in count(1) if list(islice(run(program, a), 20)) == [0, 1] * 10)

def part_2(program):
    return "Merry Christmas!"

with open("2016/Day25_input.txt") as f:
    program = [line.split() for line in f.read().splitlines()]

    print(f"Part 1: {part_1(program)}")
    print(f"Part 2: {part_2(program)}")
