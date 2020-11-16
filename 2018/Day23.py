import re
from heapq import heappush, heappop

def in_range(bots, corner, size):
    return sum(sum(max(c - v, 0, v - (c + size - 1)) for c,v in zip(corner, bot)) <= bot[3]
               for bot in bots)

def part_1(input):
    x, y, z, r = max(input, key=lambda bot: bot[3])
    return sum(abs(x-a) + abs(y-b) + abs(z-c) <= r for a,b,c,_ in input)

def part_2(input):
    size = 1
    while size < max(max(abs(v) for v in bot[:3]) for bot in input):
        size *= 2
    queue = [(-len(input), 0, 2 * size, (-size, -size, -size))]
    while queue:
        _, distance, size, corner = heappop(queue)
        if size == 1:
            return distance
        size //= 2
        for dx in (0, size):
            for dy in (0, size):
                for dz in (0, size):
                    box = (corner[0] + dx, corner[1] + dy, corner[2] + dz)
                    heappush(queue, (-in_range(input, box, size),
                                     sum(max(c, 0, -(c + size - 1)) for c in box),
                                     size, box))

with open("2018/Day23_input.txt") as f:
    input = [tuple(int(v) for v in re.findall(r'-?\d+', line)) for line in f.read().splitlines()]

    print(f"Part 1: {part_1(input)}")
    print(f"Part 2: {part_2(input)}")
