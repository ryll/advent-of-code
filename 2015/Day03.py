MOVES = {'^': (0,1), 'v': (0,-1), '<': (-1,0), '>': (1,0)}

def visit(moves):
    x = y = 0
    houses = {(0,0)}
    for c in moves:
        dx,dy = MOVES[c]
        x,y = x+dx, y+dy
        houses.add((x,y))
    return houses

def part_1(input):
    return len(visit(input))

def part_2(input):
    return len(visit(input[::2]) | visit(input[1::2]))

with open("2015/Day03_input.txt") as f:
    input = f.read().strip()

    print(f"Part 1: {part_1(input)}")
    print(f"Part 2: {part_2(input)}")
