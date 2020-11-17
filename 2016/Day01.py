def walk(instructions, first_repeat):
    x, y, dx, dy = 0, 0, 0, 1
    visited = {(0,0)}
    for turn,blocks in instructions:
        dx, dy = (dy, -dx) if turn == 'R' else (-dy, dx)
        for _ in range(blocks):
            x, y = x+dx, y+dy
            if first_repeat and (x,y) in visited:
                return abs(x) + abs(y)
            visited.add((x,y))
    return abs(x) + abs(y)

def part_1(instructions):
    return walk(instructions, False)

def part_2(instructions):
    return walk(instructions, True)

with open("2016/Day01_input.txt") as f:
    instructions = [(step[0], int(step[1:])) for step in f.read().strip().split(', ')]

    print(f"Part 1: {part_1(instructions)}")
    print(f"Part 2: {part_2(instructions)}")
