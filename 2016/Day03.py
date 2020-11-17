def possible(sides):
    a, b, c = sorted(sides)
    return a + b > c

def part_1(triangles):
    return sum(possible(t) for t in triangles)

def part_2(triangles):
    return sum(possible([triangles[i+k][j] for k in range(3)])
               for i in range(0, len(triangles), 3) for j in range(3))

with open("2016/Day03_input.txt") as f:
    triangles = [[int(v) for v in line.split()] for line in f.read().splitlines()]

    print(f"Part 1: {part_1(triangles)}")
    print(f"Part 2: {part_2(triangles)}")
