from collections import defaultdict, deque

def value(registers, x):
    return registers[x] if x.isalpha() else int(x)

def part_1(input):
    registers, i, sound = defaultdict(int), 0, None
    while 0 <= i < len(input):
        op, *args = input[i]
        if op == 'snd':   sound = value(registers, args[0])
        elif op == 'set': registers[args[0]] = value(registers, args[1])
        elif op == 'add': registers[args[0]] += value(registers, args[1])
        elif op == 'mul': registers[args[0]] *= value(registers, args[1])
        elif op == 'mod': registers[args[0]] %= value(registers, args[1])
        elif op == 'rcv' and value(registers, args[0]):
            return sound
        elif op == 'jgz' and value(registers, args[0]) > 0:
            i += value(registers, args[1]) - 1
        i += 1

def run(program, program_id, inbox, outbox):
    registers, i = defaultdict(int), 0
    registers['p'] = program_id
    while 0 <= i < len(program):
        op, *args = program[i]
        if op == 'snd':
            outbox.append(value(registers, args[0]))
            yield 'send'
        elif op == 'rcv':
            while not inbox:
                yield 'wait'
            registers[args[0]] = inbox.popleft()
        elif op == 'set': registers[args[0]] = value(registers, args[1])
        elif op == 'add': registers[args[0]] += value(registers, args[1])
        elif op == 'mul': registers[args[0]] *= value(registers, args[1])
        elif op == 'mod': registers[args[0]] %= value(registers, args[1])
        elif op == 'jgz' and value(registers, args[0]) > 0:
            i += value(registers, args[1]) - 1
        i += 1

def part_2(input):
    a, b = deque(), deque()
    programs = [run(input, 0, a, b), run(input, 1, b, a)]
    sends = 0
    while True:
        stuck = 0
        for id,program in enumerate(programs):
            state = next(program, 'done')
            sends += state == 'send' and id == 1
            stuck += state in ('wait', 'done')
        if stuck == 2:
            return sends

with open("2017/Day18_input.txt") as f:
    input = [line.split() for line in f.read().splitlines() if line]

    print(f"Part 1: {part_1(input)}")
    print(f"Part 2: {part_2(input)}")
