DELTAS = {'R': (1,0), 'L': (-1,0), 'U': (0,-1), 'D': (0,1)}

def lagoon(plan):
    x, y, doubled, perimeter = 0, 0, 0, 0
    for direction,length in plan:
        dx, dy = DELTAS[direction]
        nx, ny = x + dx*length, y + dy*length
        doubled += x*ny - nx*y
        perimeter += length
        x, y = nx, ny
    return abs(doubled)//2 + perimeter//2 + 1

def part_1(input):
    return lagoon([(direction, int(length)) for direction,length,_ in input])

def part_2(input):
    return lagoon([('RDLU'[int(colour[7])], int(colour[2:7], 16)) for _,_,colour in input])

with open("2023/Day18_input.txt") as f:
    input = [line.split() for line in f.read().splitlines()]

    print(f"Part 1: {part_1(input)}")
    print(f"Part 2: {part_2(input)}")
