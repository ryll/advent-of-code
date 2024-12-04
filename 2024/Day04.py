DIRS = [(di,dj) for di in (-1,0,1) for dj in (-1,0,1) if (di,dj) != (0,0)]

def part_1(grid):
    return sum(all(grid.get((i+k*di, j+k*dj)) == c for k,c in enumerate('XMAS'))
               for i,j in grid for di,dj in DIRS)

def part_2(grid):
    return sum(c == 'A'
               and {grid.get((i-1,j-1)), grid.get((i+1,j+1))} == {'M','S'}
               and {grid.get((i-1,j+1)), grid.get((i+1,j-1))} == {'M','S'}
               for (i,j),c in grid.items())

with open("2024/Day04_input.txt") as f:
    grid = {(i,j): c for i,row in enumerate(f.read().split()) for j,c in enumerate(row)}

    print(f"Part 1: {part_1(grid)}")
    print(f"Part 2: {part_2(grid)}")
