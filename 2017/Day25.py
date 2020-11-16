import re

def part_1(state, steps, rules):
    tape, cursor = set(), 0
    for _ in range(steps):
        write, move, state = rules[(state, cursor in tape)]
        if write:
            tape.add(cursor)
        else:
            tape.discard(cursor)
        cursor += move
    return len(tape)

def part_2(state, steps, rules):
    return "Merry Christmas!"

with open("2017/Day25_input.txt") as f:
    header, *blocks = f.read().split("\n\n")
    state = re.search(r'state (\w+)', header).group(1)
    steps = int(re.search(r'(\d+) steps', header).group(1))
    rules = {}
    for block in blocks:
        lines = [line.strip() for line in block.splitlines() if line.strip()]
        name = re.search(r'state (\w+)', lines[0]).group(1)
        for offset in (1, 5):
            rules[(name, lines[offset][-2] == '1')] = (
                lines[offset+1][-2] == '1',
                1 if 'right' in lines[offset+2] else -1,
                re.search(r'state (\w+)', lines[offset+3]).group(1))

    print(f"Part 1: {part_1(state, steps, rules)}")
    print(f"Part 2: {part_2(state, steps, rules)}")
