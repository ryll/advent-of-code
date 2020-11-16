import re
from collections import Counter

def simulate(input, steps, collide):
    particles = {i: [list(v) for v in vectors] for i,vectors in enumerate(input)}
    for _ in range(steps):
        for p,v,a in particles.values():
            for k in range(3):
                v[k] += a[k]
                p[k] += v[k]
        if collide:
            positions = Counter(tuple(p) for p,_,_ in particles.values())
            particles = {i: q for i,q in particles.items() if positions[tuple(q[0])] == 1}
    return particles

def part_1(input):
    particles = simulate(input, 500, False)
    return min(particles, key=lambda i: sum(abs(v) for v in particles[i][0]))

def part_2(input):
    return len(simulate(input, 500, True))

with open("2017/Day20_input.txt") as f:
    input = [[tuple(int(v) for v in vector.split(',')) for vector in re.findall(r'<(.*?)>', line)]
             for line in f.read().splitlines() if line]

    print(f"Part 1: {part_1(input)}")
    print(f"Part 2: {part_2(input)}")
