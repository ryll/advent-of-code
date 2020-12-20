from math import isqrt, prod

MONSTER = ["                  # ",
           "#    ##    ##    ###",
           " #  #  #  #  #  #   "]

def orientations(tile):
    for _ in range(4):
        tile = [''.join(c) for c in zip(*tile[::-1])]
        yield tile
        yield tile[::-1]

def edges(tile):
    return [tile[0], tile[-1], ''.join(r[0] for r in tile), ''.join(r[-1] for r in tile)]

def corners(input):
    counts = {}
    for tile in input.values():
        for e in edges(tile):
            counts[min(e, e[::-1])] = counts.get(min(e, e[::-1]), 0) + 1
    return [i for i,tile in input.items() if sum(counts[min(e, e[::-1])] == 1 for e in edges(tile)) == 2]

def assemble(input):
    counts = {}
    for tile in input.values():
        for e in edges(tile):
            counts[min(e, e[::-1])] = counts.get(min(e, e[::-1]), 0) + 1
    unique = lambda e: counts[min(e, e[::-1])] == 1
    col = lambda t,i: ''.join(r[i] for r in t)

    n, grid, left = isqrt(len(input)), [], dict(input)
    for i in range(n):
        row = []
        for j in range(n):
            if not i and not j:
                key = corners(input)[0]
                tile = next(t for t in orientations(left[key]) if unique(t[0]) and unique(col(t,0)))
            elif not j:
                key, tile = next((k,t) for k,v in left.items() for t in orientations(v) if t[0] == grid[i-1][0][-1])
            else:
                key, tile = next((k,t) for k,v in left.items() for t in orientations(v) if col(t,0) == col(row[-1],-1))
            left.pop(key)
            row.append(tile)
        grid.append(row)

    return [''.join(tile[r][1:-1] for tile in row) for row in grid for r in range(1, len(row[0])-1)]

def part_1(input):
    return prod(corners(input))

def part_2(input):
    image = assemble(input)
    offsets = [(i,j) for i,row in enumerate(MONSTER) for j,c in enumerate(row) if c == '#']
    for view in orientations(image):
        found = sum(all(view[i+di][j+dj] == '#' for di,dj in offsets)
                    for i in range(len(view)-len(MONSTER)+1)
                    for j in range(len(view[0])-len(MONSTER[0])+1))
        if found:
            return sum(row.count('#') for row in view) - found*len(offsets)

with open("2020/Day20_input.txt") as f:
    input = {int(block.splitlines()[0][5:-1]): block.splitlines()[1:] for block in f.read().split("\n\n")}

    print(f"Part 1: {part_1(input)}")
    print(f"Part 2: {part_2(input)}")
