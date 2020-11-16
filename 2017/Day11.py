DIRECTIONS = {'n': (0,1,-1), 's': (0,-1,1), 'ne': (1,0,-1),
              'sw': (-1,0,1), 'nw': (-1,1,0), 'se': (1,-1,0)}

def walk(input):
    x = y = z = 0
    for step in input:
        dx, dy, dz = DIRECTIONS[step]
        x, y, z = x+dx, y+dy, z+dz
        yield (abs(x) + abs(y) + abs(z)) // 2

def part_1(input):
    return list(walk(input))[-1]

def part_2(input):
    return max(walk(input))

with open("2017/Day11_input.txt") as f:
    input = f.read().strip().split(',')

    print(f"Part 1: {part_1(input)}")
    print(f"Part 2: {part_2(input)}")
