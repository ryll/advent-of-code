import sys

SLOPES = {'>': (1,0), '<': (-1,0), 'v': (0,1), '^': (0,-1)}
DELTAS = ((1,0), (-1,0), (0,1), (0,-1))

def graph(grid, slopes):
    h, w = len(grid), len(grid[0])
    start, end = (grid[0].index('.'), 0), (grid[-1].index('.'), h-1)
    open_cell = lambda x,y: 0 <= x < w and 0 <= y < h and grid[y][x] != '#'
    junctions = {start, end} | {(x,y) for y in range(h) for x in range(w) if open_cell(x,y)
                                and sum(open_cell(x+dx, y+dy) for dx,dy in DELTAS) > 2}
    edges = {j: {} for j in junctions}
    for junction in junctions:
        stack, seen = [(junction, 0)], {junction}
        while stack:
            (x,y), distance = stack.pop()
            if distance and (x,y) in junctions:
                edges[junction][(x,y)] = distance
                continue
            deltas = [SLOPES[grid[y][x]]] if slopes and grid[y][x] in SLOPES else DELTAS
            for dx,dy in deltas:
                if open_cell(x+dx, y+dy) and (x+dx, y+dy) not in seen:
                    seen.add((x+dx, y+dy))
                    stack.append(((x+dx, y+dy), distance+1))
    return edges, start, end

def longest(edges, node, end, seen):
    if node == end:
        return 0
    seen.add(node)
    best = max((distance + walk for n,distance in edges[node].items() if n not in seen
                and (walk := longest(edges, n, end, seen)) > -1), default=-1)
    seen.remove(node)
    return best

def hike(grid, slopes):
    edges, start, end = graph(grid, slopes)
    return longest(edges, start, end, set())

def part_1(grid):
    return hike(grid, True)

def part_2(grid):
    return hike(grid, False)

with open("2023/Day23_input.txt") as f:
    grid = f.read().splitlines()

    sys.setrecursionlimit(10000)
    print(f"Part 1: {part_1(grid)}")
    print(f"Part 2: {part_2(grid)}")
