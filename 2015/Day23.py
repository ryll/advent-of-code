def run(input, a):
    regs = {'a': a, 'b': 0}
    i = 0
    while 0 <= i < len(input):
        op, *args = input[i]
        if op == 'hlf':
            regs[args[0]] //= 2
        elif op == 'tpl':
            regs[args[0]] *= 3
        elif op == 'inc':
            regs[args[0]] += 1
        elif op == 'jmp':
            i += int(args[0])
            continue
        elif (op == 'jie' and regs[args[0]] % 2 == 0) or (op == 'jio' and regs[args[0]] == 1):
            i += int(args[1])
            continue
        i += 1
    return regs['b']

def part_1(input):
    return run(input, 0)

def part_2(input):
    return run(input, 1)

with open("2015/Day23_input.txt") as f:
    input = [line.replace(',', '').split() for line in f.read().splitlines()]

    print(f"Part 1: {part_1(input)}")
    print(f"Part 2: {part_2(input)}")
