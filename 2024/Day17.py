import re

def run(program, a, b=0, c=0):
    out, ip = [], 0
    while ip < len(program) - 1:
        op, arg = program[ip], program[ip+1]
        combo = (0, 1, 2, 3, a, b, c, 0)[arg]
        if op == 0:   a >>= combo
        elif op == 1: b ^= arg
        elif op == 2: b = combo % 8
        elif op == 4: b ^= c
        elif op == 5: out.append(combo % 8)
        elif op == 6: b = a >> combo
        elif op == 7: c = a >> combo
        elif op == 3 and a:
            ip = arg
            continue
        ip += 2
    return out

def part_1(registers, program):
    return ','.join(str(v) for v in run(program, *registers))

def part_2(registers, program):
    candidates = [0]
    for i in reversed(range(len(program))):
        candidates = [a for candidate in candidates for a in range(8*candidate, 8*candidate + 8)
                      if run(program, a) == program[i:]]
    return min(candidates)

with open("2024/Day17_input.txt") as f:
    register_block, program_block = f.read().split("\n\n")
    registers = [int(v) for v in re.findall(r'\d+', register_block)]
    program = [int(v) for v in re.findall(r'\d+', program_block)]

    print(f"Part 1: {part_1(registers, program)}")
    print(f"Part 2: {part_2(registers, program)}")
