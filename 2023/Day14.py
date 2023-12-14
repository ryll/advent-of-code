def roll(line):
    return '#'.join(''.join(sorted(part, reverse=True)) for part in line.split('#'))

def north(grid):
    return tuple(''.join(row) for row in zip(*(roll(''.join(col)) for col in zip(*grid))))

def clockwise(grid):
    return tuple(''.join(row) for row in zip(*grid[::-1]))

def load(grid):
    return sum(row.count('O') * (len(grid) - y) for y,row in enumerate(grid))

def part_1(grid):
    return load(north(grid))

def part_2(grid):
    seen, cycles = {}, 1000000000
    for i in range(cycles):
        if grid in seen:
            grid = list(seen)[seen[grid] + (cycles - seen[grid]) % (i - seen[grid])]
            break
        seen[grid] = i
        for _ in range(4):
            grid = clockwise(north(grid))
    return load(grid)

with open("2023/Day14_input.txt") as f:
    grid = tuple(f.read().splitlines())

    print(f"Part 1: {part_1(grid)}")
    print(f"Part 2: {part_2(grid)}")
