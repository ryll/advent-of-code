def walk(grid, steps):
    h, w = len(grid), len(grid[0])
    start = next((x,y) for y,line in enumerate(grid)
                 for x,c in enumerate(line) if c == 'S')
    frontier, seen = {start}, {start: 0}
    for step in range(1, steps+1):
        frontier = {(nx,ny) for x,y in frontier
                    for nx,ny in ((x+1,y), (x-1,y), (x,y+1), (x,y-1))
                    if grid[ny % h][nx % w] != '#' and (nx,ny) not in seen}
        seen.update(dict.fromkeys(frontier, step))
    return sum(1 for s in seen.values() if s % 2 == steps % 2)

def part_1(grid):
    return walk(grid, 64)

def part_2(grid):
    size, steps = len(grid), 26501365
    a, b, c = (walk(grid, steps % size + i*size) for i in range(3))
    n = steps // size
    return a + n*(b-a) + n*(n-1)//2 * (c - 2*b + a)

with open("2023/Day21_input.txt") as f:
    grid = f.read().splitlines()

    print(f"Part 1: {part_1(grid)}")
    print(f"Part 2: {part_2(grid)}")
