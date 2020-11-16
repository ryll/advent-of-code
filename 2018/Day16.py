import re

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

def matches(before, instruction, after):
    _, a, b, c = instruction
    names = set()
    for name,op in OPS.items():
        registers = list(before)
        try:
            registers[c] = op(registers, a, b)
        except IndexError:
            continue
        if tuple(registers) == after:
            names.add(name)
    return names

def part_1(samples, program):
    return sum(len(matches(*sample)) >= 3 for sample in samples)

def part_2(samples, program):
    candidates = {}
    for before,instruction,after in samples:
        code = instruction[0]
        candidates[code] = candidates.get(code, set(OPS)) & matches(before, instruction, after)
    mapping = {}
    while candidates:
        code, names = next((c,n) for c,n in candidates.items() if len(n) == 1)
        mapping[code] = name = names.pop()
        del candidates[code]
        for other in candidates.values():
            other.discard(name)
    registers = [0, 0, 0, 0]
    for code,a,b,c in program:
        registers[c] = OPS[mapping[code]](registers, a, b)
    return registers[0]

with open("2018/Day16_input.txt") as f:
    sample_text, program_text = f.read().split("\n\n\n\n")
    samples = []
    for block in sample_text.split("\n\n"):
        before, instruction, after = block.splitlines()
        samples.append((tuple(int(v) for v in re.findall(r'\d+', before)),
                        tuple(int(v) for v in instruction.split()),
                        tuple(int(v) for v in re.findall(r'\d+', after))))
    program = [tuple(int(v) for v in line.split()) for line in program_text.splitlines() if line]

    print(f"Part 1: {part_1(samples, program)}")
    print(f"Part 2: {part_2(samples, program)}")
