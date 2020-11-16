import re
import sys

sys.setrecursionlimit(20000)

def supported(clay, settled, p):
    return p in clay or p in settled

def flow(clay, water, settled, visited, y, x, max_y):
    if y > max_y or (y,x) in visited:
        return
    visited.add((y,x))
    water.add((y,x))
    if not supported(clay, settled, (y+1,x)):
        flow(clay, water, settled, visited, y+1, x, max_y)
        if not supported(clay, settled, (y+1,x)):
            return
    left = right = x
    while (y,left-1) not in clay and supported(clay, settled, (y+1,left-1)):
        left -= 1
    while (y,right+1) not in clay and supported(clay, settled, (y+1,right+1)):
        right += 1
    water.update((y,i) for i in range(left, right+1))
    visited.update((y,i) for i in range(left, right+1))
    if (y,left-1) in clay and (y,right+1) in clay:
        settled.update((y,i) for i in range(left, right+1))
    else:
        if (y,left-1) not in clay:
            flow(clay, water, settled, visited, y, left-1, max_y)
        if (y,right+1) not in clay:
            flow(clay, water, settled, visited, y, right+1, max_y)

def simulate(clay):
    min_y, max_y = min(y for y,_ in clay), max(y for y,_ in clay)
    water, settled = set(), set()
    while True:
        before = len(settled)
        flow(clay, water, settled, set(), min_y, 500, max_y)
        if len(settled) == before:
            return {(y,x) for y,x in water if min_y <= y <= max_y}, settled

def part_1(input):
    return len(simulate(input)[0])

def part_2(input):
    return len(simulate(input)[1])

with open("2018/Day17_input.txt") as f:
    input = set()
    for line in f.read().splitlines():
        fixed, lo, hi = (int(v) for v in re.findall(r'\d+', line))
        for v in range(lo, hi+1):
            input.add((v, fixed) if line[0] == 'x' else (fixed, v))

    print(f"Part 1: {part_1(input)}")
    print(f"Part 2: {part_2(input)}")
