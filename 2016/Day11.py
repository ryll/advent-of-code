import re
from collections import deque
from itertools import combinations

TOP = 3

def safe(pairs):
    generators = {generator for generator,_ in pairs}
    return all(chip == generator or chip not in generators for generator,chip in pairs)

def steps(pairs):
    start = (0, tuple(sorted(pairs)))
    queue, seen = deque([(start, 0)]), {start}
    while queue:
        (elevator, state), moved = queue.popleft()
        if all(floor == TOP for pair in state for floor in pair):
            return moved
        carried = [(i,j) for i,pair in enumerate(state) for j in (0,1) if pair[j] == elevator]
        for load in [*combinations(carried, 1), *combinations(carried, 2)]:
            for floor in (elevator+1, elevator-1):
                if not 0 <= floor <= TOP:
                    continue
                moving = [list(pair) for pair in state]
                for i,j in load:
                    moving[i][j] = floor
                new = (floor, tuple(sorted(tuple(pair) for pair in moving)))
                if new not in seen and safe(new[1]):
                    seen.add(new)
                    queue.append((new, moved+1))

def part_1(pairs):
    return steps(pairs)

def part_2(pairs):
    return steps(pairs + [(0,0), (0,0)])

with open("2016/Day11_input.txt") as f:
    generators, chips = {}, {}
    for floor,line in enumerate(f.read().splitlines()):
        for element in re.findall(r'(\w+) generator', line):
            generators[element] = floor
        for element in re.findall(r'(\w+)-compatible microchip', line):
            chips[element] = floor
    pairs = [(generators[element], chips[element]) for element in generators]

    print(f"Part 1: {part_1(pairs)}")
    print(f"Part 2: {part_2(pairs)}")
