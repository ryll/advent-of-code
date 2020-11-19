import re

WIDTH, HEIGHT = 50, 6

def display(instructions):
    lit = set()
    for line in instructions:
        a, b = (int(v) for v in re.findall(r'\d+', line))
        if line.startswith('rect'):
            lit |= {(x,y) for x in range(a) for y in range(b)}
        elif line.startswith('rotate row'):
            lit = {((x+b) % WIDTH, y) if y == a else (x,y) for x,y in lit}
        else:
            lit = {(x, (y+b) % HEIGHT) if x == a else (x,y) for x,y in lit}
    return lit

def part_1(instructions):
    return len(display(instructions))

def part_2(instructions):
    lit = display(instructions)
    return '\n' + '\n'.join(''.join('#' if (x,y) in lit else ' ' for x in range(WIDTH))
                            for y in range(HEIGHT))

with open("2016/Day08_input.txt") as f:
    instructions = f.read().splitlines()

    print(f"Part 1: {part_1(instructions)}")
    print(f"Part 2: {part_2(instructions)}")
