import re

def run(input, actions):
    grid = {}
    for action, x1, y1, x2, y2 in input:
        change = actions[action]
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                grid[x,y] = change(grid.get((x,y), 0))
    return sum(grid.values())

def part_1(input):
    return run(input, {'turn on': lambda v: 1, 'turn off': lambda v: 0, 'toggle': lambda v: 1 - v})

def part_2(input):
    return run(input, {'turn on': lambda v: v + 1, 'turn off': lambda v: max(0, v - 1), 'toggle': lambda v: v + 2})

with open("2015/Day06_input.txt") as f:
    input = [(m[1], *(int(x) for x in m.groups()[1:]))
             for m in re.finditer(r'(turn on|turn off|toggle) (\d+),(\d+) through (\d+),(\d+)', f.read())]

    print(f"Part 1: {part_1(input)}")
    print(f"Part 2: {part_2(input)}")
