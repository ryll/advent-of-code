from itertools import count

def move(grid, rows, cols, herd, di, dj):
    moved = {}
    for (i,j),c in grid.items():
        target = ((i+di) % rows, (j+dj) % cols)
        moved[(i,j) if c != herd or target in grid else target] = c
    return moved

def part_1(grid, rows, cols):
    for step in count(1):
        new = move(move(grid, rows, cols, '>', 0, 1), rows, cols, 'v', 1, 0)
        if new == grid:
            return step
        grid = new

def part_2(grid, rows, cols):
    return "Merry Christmas!"

with open("2021/Day25_input.txt") as f:
    lines = f.read().split()
    rows, cols = len(lines), len(lines[0])
    grid = {(i,j): c for i,row in enumerate(lines) for j,c in enumerate(row) if c != '.'}

    print(f"Part 1: {part_1(grid, rows, cols)}")
    print(f"Part 2: {part_2(grid, rows, cols)}")
