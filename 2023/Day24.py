from fractions import Fraction
from itertools import combinations

def cross(a, b):
    return [a[1]*b[2] - a[2]*b[1], a[2]*b[0] - a[0]*b[2], a[0]*b[1] - a[1]*b[0]]

def matrix(a):
    return [[0, -a[2], a[1]], [a[2], 0, -a[0]], [-a[1], a[0], 0]]

def solve(system):
    n = len(system)
    system = [[Fraction(v) for v in row] for row in system]
    for i in range(n):
        pivot = next(r for r in range(i, n) if system[r][i])
        system[i], system[pivot] = system[pivot], system[i]
        system[i] = [v / system[i][i] for v in system[i]]
        for r in range(n):
            if r != i and system[r][i]:
                system[r] = [a - system[r][i]*b for a,b in zip(system[r], system[i])]
    return [row[n] for row in system]

def part_1(input):
    lo, hi = 200000000000000, 400000000000000
    total = 0
    for (p,v),(q,w) in combinations(input, 2):
        det = v[0]*w[1] - v[1]*w[0]
        if not det:
            continue
        t = Fraction((q[0]-p[0])*w[1] - (q[1]-p[1])*w[0], det)
        s = Fraction((q[0]-p[0])*v[1] - (q[1]-p[1])*v[0], det)
        x, y = p[0] + t*v[0], p[1] + t*v[1]
        total += t > 0 and s > 0 and lo <= x <= hi and lo <= y <= hi
    return total

def part_2(input):
    (p0,v0), (p1,v1), (p2,v2) = input[:3]
    system = []
    for p,v in ((p1,v1), (p2,v2)):
        dv = [b-a for a,b in zip(v0, v)]
        dp = [b-a for a,b in zip(p0, p)]
        rhs = [a-b for a,b in zip(cross(p, v), cross(p0, v0))]
        system += [[-a for a in left] + right + [r]
                   for left,right,r in zip(matrix(dv), matrix(dp), rhs)]
    return sum(solve(system)[:3])

with open("2023/Day24_input.txt") as f:
    input = [tuple([int(v) for v in half.split(',')] for half in line.split(' @ '))
             for line in f.read().splitlines()]

    print(f"Part 1: {part_1(input)}")
    print(f"Part 2: {part_2(input)}")
