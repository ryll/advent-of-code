from collections import Counter
from itertools import permutations, product

ROTATIONS = [(perm, signs) for perm in permutations(range(3)) for signs in product((1,-1), repeat=3)
             if (1 if perm in ((0,1,2),(1,2,0),(2,0,1)) else -1) * signs[0]*signs[1]*signs[2] == 1]

def rotate(p, rotation):
    perm, signs = rotation
    return (signs[0]*p[perm[0]], signs[1]*p[perm[1]], signs[2]*p[perm[2]])

def match(known, scanner):
    for rotation in ROTATIONS:
        rotated = [rotate(p, rotation) for p in scanner]
        offset, n = Counter((a[0]-b[0], a[1]-b[1], a[2]-b[2])
                            for a in known for b in rotated).most_common(1)[0]
        if n >= 12:
            return offset, {(b[0]+offset[0], b[1]+offset[1], b[2]+offset[2]) for b in rotated}

def solve(input):
    beacons, positions, todo, frontier = set(input[0]), [(0,0,0)], list(input[1:]), [set(input[0])]
    while todo:
        new = []
        for known in frontier:
            for scanner in todo[:]:
                if found := match(known, scanner):
                    offset, placed = found
                    todo.remove(scanner)
                    positions.append(offset)
                    beacons |= placed
                    new.append(placed)
        frontier = new
    return beacons, positions

def part_1(input):
    return len(solve(input)[0])

def part_2(input):
    positions = solve(input)[1]
    return max(sum(abs(x-y) for x,y in zip(a,b)) for a in positions for b in positions)

with open("2021/Day19_input.txt") as f:
    input = [[tuple(int(v) for v in line.split(',')) for line in block.splitlines()[1:]]
             for block in f.read().split("\n\n")]

    print(f"Part 1: {part_1(input)}")
    print(f"Part 2: {part_2(input)}")
