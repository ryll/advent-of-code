from itertools import count

def step(grid):
    for p in grid:
        grid[p] += 1
    flashed = set()
    while (ready := [p for p,e in grid.items() if e > 9 and p not in flashed]):
        for i,j in ready:
            flashed.add((i,j))
            for di in (-1,0,1):
                for dj in (-1,0,1):
                    if (i+di, j+dj) in grid:
                        grid[i+di, j+dj] += 1
    for p in flashed:
        grid[p] = 0
    return len(flashed)

def part_1(input):
    grid = dict(input)
    return sum(step(grid) for _ in range(100))

def part_2(input):
    grid = dict(input)
    return next(i for i in count(1) if step(grid) == len(grid))

with open("2021/Day11_input.txt") as f:
    input = {(i,j): int(c) for i,row in enumerate(f.read().split()) for j,c in enumerate(row)}

    print(f"Part 1: {part_1(input)}")
    print(f"Part 2: {part_2(input)}")
