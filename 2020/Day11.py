DIRECTIONS = [(di,dj) for di in (-1,0,1) for dj in (-1,0,1) if (di,dj) != (0,0)]

def neighbours(input, i, j, far):
    for di,dj in DIRECTIONS:
        x, y = i+di, j+dj
        while far and input.get((x,y)) == '.':
            x, y = x+di, y+dj
        yield input.get((x,y))

def run(input, limit, far):
    while True:
        new = {}
        for (i,j),seat in input.items():
            taken = sum(s == '#' for s in neighbours(input, i, j, far))
            new[i,j] = '#' if seat == 'L' and not taken else 'L' if seat == '#' and taken >= limit else seat
        if new == input:
            return sum(s == '#' for s in input.values())
        input = new

def part_1(input):
    return run(input, 4, False)

def part_2(input):
    return run(input, 5, True)

with open("2020/Day11_input.txt") as f:
    input = {(i,j): c for i,row in enumerate(f.read().split()) for j,c in enumerate(row)}

    print(f"Part 1: {part_1(input)}")
    print(f"Part 2: {part_2(input)}")
