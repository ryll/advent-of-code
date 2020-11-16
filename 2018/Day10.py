import re

def move(input, t):
    return [(x + t*dx, y + t*dy) for x,y,dx,dy in input]

def height(points):
    return max(y for _,y in points) - min(y for _,y in points)

def converge(input):
    return min(range(20000), key=lambda t: height(move(input, t)))

def part_1(input):
    points = set(move(input, converge(input)))
    return '\n' + '\n'.join(''.join('#' if (x,y) in points else ' '
                                    for x in range(min(x for x,_ in points), max(x for x,_ in points)+1))
                            for y in range(min(y for _,y in points), max(y for _,y in points)+1))

def part_2(input):
    return converge(input)

with open("2018/Day10_input.txt") as f:
    input = [tuple(int(v) for v in re.findall(r'-?\d+', line)) for line in f.read().splitlines()]

    print(f"Part 1: {part_1(input)}")
    print(f"Part 2: {part_2(input)}")
