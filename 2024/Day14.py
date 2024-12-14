import re
from collections import Counter
from math import prod

WIDTH, HEIGHT = 101, 103

def positions(robots, t):
    return [((px + t*vx) % WIDTH, (py + t*vy) % HEIGHT) for px,py,vx,vy in robots]

def part_1(robots):
    quadrants = Counter((x < WIDTH//2, y < HEIGHT//2) for x,y in positions(robots, 100)
                        if x != WIDTH//2 and y != HEIGHT//2)
    return prod(quadrants.values())

def part_2(robots):
    return next(t for t in range(WIDTH*HEIGHT) if len(set(positions(robots, t))) == len(robots))

with open("2024/Day14_input.txt") as f:
    robots = [[int(v) for v in re.findall(r'-?\d+', line)] for line in f.read().splitlines()]

    print(f"Part 1: {part_1(robots)}")
    print(f"Part 2: {part_2(robots)}")
