def summits(grid, start):
    found, stack = [], [start]
    while stack:
        i, j = stack.pop()
        if grid[i,j] == 9:
            found.append((i,j))
            continue
        stack += [p for p in ((i-1,j), (i+1,j), (i,j-1), (i,j+1))
                  if grid.get(p) == grid[i,j] + 1]
    return found

def part_1(grid):
    return sum(len(set(summits(grid, p))) for p,h in grid.items() if h == 0)

def part_2(grid):
    return sum(len(summits(grid, p)) for p,h in grid.items() if h == 0)

with open("2024/Day10_input.txt") as f:
    grid = {(i,j): int(c) for i,row in enumerate(f.read().split()) for j,c in enumerate(row)}

    print(f"Part 1: {part_1(grid)}")
    print(f"Part 2: {part_2(grid)}")
