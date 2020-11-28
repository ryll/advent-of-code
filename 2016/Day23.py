MULTIPLY = ['cpy', 'inc', 'dec', 'jnz', 'dec', 'jnz']

def run(program, registers):
    program = [list(instruction) for instruction in program]
    def value(a):
        return registers[a] if a in registers else int(a)
    ip = 0
    while 0 <= ip < len(program):
        block = program[ip:ip+6]
        if ([instruction[0] for instruction in block] == MULTIPLY
                and block[0][2] == block[2][1] == block[3][1] and block[4][1] == block[5][1]
                and block[3][2] == '-2' and block[5][2] == '-5' and block[1][1] in registers):
            registers[block[1][1]] += value(block[0][1]) * registers[block[4][1]]
            registers[block[0][2]] = registers[block[4][1]] = 0
            ip += 6
            continue
        op, *args = program[ip]
        if op == 'cpy' and args[1] in registers:
            registers[args[1]] = value(args[0])
        elif op == 'inc' and args[0] in registers:
            registers[args[0]] += 1
        elif op == 'dec' and args[0] in registers:
            registers[args[0]] -= 1
        elif op == 'tgl':
            target = ip + value(args[0])
            if 0 <= target < len(program):
                instruction = program[target]
                if len(instruction) == 2:
                    instruction[0] = 'dec' if instruction[0] == 'inc' else 'inc'
                else:
                    instruction[0] = 'cpy' if instruction[0] == 'jnz' else 'jnz'
        elif op == 'jnz' and value(args[0]):
            ip += value(args[1]) - 1
        ip += 1
    return registers['a']

def part_1(program):
    return run(program, dict.fromkeys('abcd', 0) | {'a': 7})

def part_2(program):
    return run(program, dict.fromkeys('abcd', 0) | {'a': 12})

with open("2016/Day23_input.txt") as f:
    program = [line.split() for line in f.read().splitlines()]

    print(f"Part 1: {part_1(program)}")
    print(f"Part 2: {part_2(program)}")
