def run(program):
    acc, i, seen = 0, 0, set()
    while i < len(program) and i not in seen:
        seen.add(i)
        op, arg = program[i]
        acc += arg * (op == 'acc')
        i += arg if op == 'jmp' else 1
    return acc, i == len(program)

def part_1(input):
    return run(input)[0]

def part_2(input):
    for i,(op,arg) in enumerate(input):
        if op == 'acc':
            continue
        acc, ended = run(input[:i] + [('jmp' if op == 'nop' else 'nop', arg)] + input[i+1:])
        if ended:
            return acc

with open("2020/Day08_input.txt") as f:
    input = [(op, int(arg)) for op,arg in (line.split() for line in f)]

    print(f"Part 1: {part_1(input)}")
    print(f"Part 2: {part_2(input)}")
