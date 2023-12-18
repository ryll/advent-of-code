from heapq import heappush, heappop

def heat_loss(grid, lo, hi):
    h, w = len(grid), len(grid[0])
    queue, seen = [(0, 0, 0, 0, 0)], set()
    while queue:
        cost, x, y, dx, dy = heappop(queue)
        if (x,y) == (w-1, h-1):
            return cost
        if (x,y,dx,dy) in seen:
            continue
        seen.add((x,y,dx,dy))
        for ndx,ndy in ((0,1), (0,-1), (1,0), (-1,0)):
            if (ndx,ndy) in ((dx,dy), (-dx,-dy)):
                continue
            step_cost = cost
            for step in range(1, hi+1):
                nx, ny = x + ndx*step, y + ndy*step
                if not (0 <= nx < w and 0 <= ny < h):
                    break
                step_cost += grid[ny][nx]
                if step >= lo:
                    heappush(queue, (step_cost, nx, ny, ndx, ndy))

def part_1(grid):
    return heat_loss(grid, 1, 3)

def part_2(grid):
    return heat_loss(grid, 4, 10)

with open("2023/Day17_input.txt") as f:
    grid = [[int(c) for c in line] for line in f.read().split()]

    print(f"Part 1: {part_1(grid)}")
    print(f"Part 2: {part_2(grid)}")
