from collections import Counter

def step(grid):
    new = {}
    for (i,j),acre in grid.items():
        adjacent = Counter(grid[(i+di,j+dj)] for di in (-1,0,1) for dj in (-1,0,1)
                           if (di,dj) != (0,0) and (i+di,j+dj) in grid)
        if acre == '.':
            new[(i,j)] = '|' if adjacent['|'] >= 3 else '.'
        elif acre == '|':
            new[(i,j)] = '#' if adjacent['#'] >= 3 else '|'
        else:
            new[(i,j)] = '#' if adjacent['#'] and adjacent['|'] else '.'
    return new

def run(grid, minutes):
    seen, minute = {}, 0
    while minute < minutes:
        key = ''.join(acre for _,acre in sorted(grid.items()))
        if key in seen:
            cycle = minute - seen[key]
            minute += (minutes - minute) // cycle * cycle
            seen = {}
            if minute >= minutes:
                break
        seen[key] = minute
        grid = step(grid)
        minute += 1
    counts = Counter(grid.values())
    return counts['|'] * counts['#']

def part_1(input):
    return run(input, 10)

def part_2(input):
    return run(input, 1000000000)

with open("2018/Day18_input.txt") as f:
    input = {(i,j): acre for i,row in enumerate(f.read().splitlines())
             for j,acre in enumerate(row)}

    print(f"Part 1: {part_1(input)}")
    print(f"Part 2: {part_2(input)}")
