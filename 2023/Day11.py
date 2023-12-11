def distances(grid, factor):
    rows = [y for y,line in enumerate(grid) if '#' not in line]
    cols = [x for x in range(len(grid[0])) if all(line[x] != '#' for line in grid)]
    galaxies = [(x + (factor-1)*sum(c < x for c in cols),
                 y + (factor-1)*sum(r < y for r in rows))
                for y,line in enumerate(grid) for x,c in enumerate(line) if c == '#']
    return sum(abs(a[0]-b[0]) + abs(a[1]-b[1])
               for i,a in enumerate(galaxies) for b in galaxies[:i])

def part_1(grid):
    return distances(grid, 2)

def part_2(grid):
    return distances(grid, 1000000)

with open("2023/Day11_input.txt") as f:
    grid = f.read().splitlines()

    print(f"Part 1: {part_1(grid)}")
    print(f"Part 2: {part_2(grid)}")
