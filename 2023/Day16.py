def energised(grid, start):
    seen, beams = set(), [start]
    while beams:
        x, y, dx, dy = beams.pop()
        x, y = x+dx, y+dy
        if not (0 <= y < len(grid) and 0 <= x < len(grid[0])) or (x,y,dx,dy) in seen:
            continue
        seen.add((x,y,dx,dy))
        c = grid[y][x]
        if c == '/':
            deltas = [(-dy,-dx)]
        elif c == '\\':
            deltas = [(dy,dx)]
        elif c == '|' and dx:
            deltas = [(0,-1), (0,1)]
        elif c == '-' and dy:
            deltas = [(-1,0), (1,0)]
        else:
            deltas = [(dx,dy)]
        beams += [(x,y,a,b) for a,b in deltas]
    return len({(x,y) for x,y,_,_ in seen})

def part_1(grid):
    return energised(grid, (-1,0,1,0))

def part_2(grid):
    h, w = len(grid), len(grid[0])
    starts = ([(-1,y,1,0) for y in range(h)] + [(w,y,-1,0) for y in range(h)] +
              [(x,-1,0,1) for x in range(w)] + [(x,h,0,-1) for x in range(w)])
    return max(energised(grid, start) for start in starts)

with open("2023/Day16_input.txt") as f:
    grid = f.read().splitlines()

    print(f"Part 1: {part_1(grid)}")
    print(f"Part 2: {part_2(grid)}")
