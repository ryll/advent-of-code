def regions(grid):
    seen = set()
    for start in grid:
        if start in seen:
            continue
        region, stack = set(), [start]
        while stack:
            i, j = stack.pop()
            if (i,j) in region:
                continue
            region.add((i,j))
            stack += [p for p in ((i-1,j), (i+1,j), (i,j-1), (i,j+1))
                      if grid.get(p) == grid[start] and p not in region]
        seen |= region
        yield region

def part_1(grid):
    return sum(len(r) * sum((i+di, j+dj) not in r for i,j in r
                            for di,dj in ((-1,0), (1,0), (0,-1), (0,1)))
               for r in regions(grid))

def part_2(grid):
    total = 0
    for region in regions(grid):
        corners = 0
        for i,j in region:
            for di,dj in ((-1,-1), (-1,1), (1,-1), (1,1)):
                side, other, diagonal = (i+di,j) in region, (i,j+dj) in region, (i+di,j+dj) in region
                corners += (not side and not other) or (side and other and not diagonal)
        total += len(region) * corners
    return total

with open("2024/Day12_input.txt") as f:
    grid = {(i,j): c for i,row in enumerate(f.read().split()) for j,c in enumerate(row)}

    print(f"Part 1: {part_1(grid)}")
    print(f"Part 2: {part_2(grid)}")
