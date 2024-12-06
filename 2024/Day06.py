def walk(grid, start):
    i, j, di, dj = *start, -1, 0
    seen = set()
    while (i, j, di, dj) not in seen:
        seen.add((i, j, di, dj))
        ahead = grid.get((i+di, j+dj))
        if ahead == '#':
            di, dj = dj, -di
        elif ahead is None:
            return {(i,j) for i,j,_,_ in seen}, False
        else:
            i, j = i+di, j+dj
    return None, True

def part_1(grid, start):
    return len(walk(grid, start)[0])

def part_2(grid, start):
    total = 0
    for pos in walk(grid, start)[0] - {start}:
        grid[pos] = '#'
        total += walk(grid, start)[1]
        grid[pos] = '.'
    return total

with open("2024/Day06_input.txt") as f:
    grid = {(i,j): c for i,row in enumerate(f.read().split()) for j,c in enumerate(row)}
    start = next(p for p,c in grid.items() if c == '^')

    print(f"Part 1: {part_1(grid, start)}")
    print(f"Part 2: {part_2(grid, start)}")
