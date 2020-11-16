def burst(input, bursts, evolved):
    grid, pos, d, infections = dict(input), (0, 0), (-1, 0), 0
    for _ in range(bursts):
        state = grid.get(pos, '.')
        if state == '.':
            d = (-d[1], d[0])
            grid[pos] = 'W' if evolved else '#'
            infections += not evolved
        elif state == 'W':
            grid[pos] = '#'
            infections += 1
        elif state == '#':
            d = (d[1], -d[0])
            grid[pos] = 'F' if evolved else '.'
        else:
            d = (-d[0], -d[1])
            grid[pos] = '.'
        pos = (pos[0] + d[0], pos[1] + d[1])
    return infections

def part_1(input):
    return burst(input, 10000, False)

def part_2(input):
    return burst(input, 10000000, True)

with open("2017/Day22_input.txt") as f:
    lines = f.read().split()
    offset = len(lines) // 2
    input = {(i - offset, j - offset): c for i,row in enumerate(lines)
             for j,c in enumerate(row) if c == '#'}

    print(f"Part 1: {part_1(input)}")
    print(f"Part 2: {part_2(input)}")
