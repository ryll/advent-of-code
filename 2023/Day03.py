import re

def numbers(grid):
    for y,line in enumerate(grid):
        for m in re.finditer(r"\d+", line):
            yield int(m.group()), {(x,j) for j in (y-1, y, y+1)
                                   for x in range(m.start()-1, m.end()+1)}

def symbols(grid):
    return {(x,y): c for y,line in enumerate(grid) for x,c in enumerate(line)
            if c != '.' and not c.isdigit()}

def part_1(grid):
    found = symbols(grid)
    return sum(n for n,cells in numbers(grid) if cells & found.keys())

def part_2(grid):
    found = symbols(grid)
    gears = {}
    for n,cells in numbers(grid):
        for cell in cells & found.keys():
            if found[cell] == '*':
                gears.setdefault(cell, []).append(n)
    return sum(ns[0]*ns[1] for ns in gears.values() if len(ns) == 2)

with open("2023/Day03_input.txt") as f:
    grid = f.read().splitlines()

    print(f"Part 1: {part_1(grid)}")
    print(f"Part 2: {part_2(grid)}")
