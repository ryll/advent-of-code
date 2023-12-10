PIPES = {'|': ((0,-1), (0,1)), '-': ((-1,0), (1,0)), 'L': ((0,-1), (1,0)),
         'J': ((0,-1), (-1,0)), '7': ((0,1), (-1,0)), 'F': ((0,1), (1,0))}

def exits(grid, x, y):
    if 0 <= y < len(grid) and 0 <= x < len(grid[y]):
        return PIPES.get(grid[y][x], ())
    return ()

def trace(grid):
    start = next((x,y) for y,line in enumerate(grid)
                 for x,c in enumerate(line) if c == 'S')
    shape = next(deltas for deltas in PIPES.values()
                 if all((-dx,-dy) in exits(grid, start[0]+dx, start[1]+dy) for dx,dy in deltas))
    loop = [start]
    (x,y), (dx,dy) = start, shape[0]
    while (x+dx, y+dy) != start:
        x, y = x+dx, y+dy
        loop.append((x,y))
        dx, dy = next(d for d in PIPES[grid[y][x]] if d != (-dx,-dy))
    return loop

def part_1(grid):
    return len(trace(grid)) // 2

def part_2(grid):
    loop = trace(grid)
    area = abs(sum(x1*y2 - x2*y1 for (x1,y1),(x2,y2) in zip(loop, loop[1:] + loop[:1]))) // 2
    return area - len(loop)//2 + 1

with open("2023/Day10_input.txt") as f:
    grid = f.read().splitlines()

    print(f"Part 1: {part_1(grid)}")
    print(f"Part 2: {part_2(grid)}")
