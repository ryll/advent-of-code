DIRS = {'^': (-1,0), 'v': (1,0), '<': (0,-1), '>': (0,1)}

def part_1(warehouse, moves):
    grid = dict(warehouse)
    i, j = next(p for p,c in grid.items() if c == '@')
    grid[i,j] = '.'
    for move in moves:
        di, dj = DIRS[move]
        target = (i+di, j+dj)
        free = target
        while grid.get(free) == 'O':
            free = (free[0]+di, free[1]+dj)
        if grid.get(free) == '.':
            grid[free] = 'O'
            grid[target] = '.'
            i, j = target
    return sum(100*i + j for (i,j),c in grid.items() if c == 'O')

def part_2(warehouse, moves):
    grid = {}
    for (i,j),c in warehouse.items():
        grid[i,2*j], grid[i,2*j+1] = {'#': '##', 'O': '[]', '.': '..', '@': '@.'}[c]
    i, j = next(p for p,c in grid.items() if c == '@')
    grid[i,j] = '.'
    for move in moves:
        di, dj = DIRS[move]
        front, pushed, blocked = {(i,j)}, set(), False
        while front and not blocked:
            ahead = set()
            for a,b in front:
                p = (a+di, b+dj)
                if grid.get(p) == '#':
                    blocked = True
                elif grid.get(p) == '[':
                    ahead |= {p, (p[0], p[1]+1)}
                elif grid.get(p) == ']':
                    ahead |= {p, (p[0], p[1]-1)}
            front = ahead - pushed
            pushed |= ahead
        if blocked:
            continue
        for a,b in sorted(pushed, key=lambda p: -(p[0]*di + p[1]*dj)):
            grid[a+di, b+dj] = grid[a,b]
            grid[a,b] = '.'
        i, j = i+di, j+dj
    return sum(100*i + j for (i,j),c in grid.items() if c == '[')

with open("2024/Day15_input.txt") as f:
    grid_block, move_block = f.read().split("\n\n")
    warehouse = {(i,j): c for i,row in enumerate(grid_block.split()) for j,c in enumerate(row)}
    moves = ''.join(move_block.split())

    print(f"Part 1: {part_1(warehouse, moves)}")
    print(f"Part 2: {part_2(warehouse, moves)}")
