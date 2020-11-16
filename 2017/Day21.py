START = ('.#.', '..#', '###')

def rotate(grid):
    return tuple(''.join(row[i] for row in reversed(grid)) for i in range(len(grid)))

def variants(grid):
    for _ in range(4):
        grid = rotate(grid)
        yield grid
        yield tuple(row[::-1] for row in grid)

def expand(input, iterations):
    grid = START
    for _ in range(iterations):
        size = 2 if len(grid) % 2 == 0 else 3
        new = []
        for i in range(len(grid) // size):
            rows = [''] * (size + 1)
            for j in range(len(grid) // size):
                block = tuple(grid[i*size + k][j*size:(j+1)*size] for k in range(size))
                for k,row in enumerate(input[block]):
                    rows[k] += row
            new += rows
        grid = tuple(new)
    return sum(row.count('#') for row in grid)

def part_1(input):
    return expand(input, 5)

def part_2(input):
    return expand(input, 18)

with open("2017/Day21_input.txt") as f:
    input = {}
    for line in f.read().splitlines():
        if line:
            source, target = (tuple(part.split('/')) for part in line.split(' => '))
            for variant in variants(source):
                input[variant] = target

    print(f"Part 1: {part_1(input)}")
    print(f"Part 2: {part_2(input)}")
