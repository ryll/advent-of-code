import re

DIRECTIONS = {'e': 2+0j, 'w': -2+0j, 'ne': 1+1j, 'nw': -1+1j, 'se': 1-1j, 'sw': -1-1j}

def part_1(input):
    return len(black(input))

def part_2(input):
    tiles = black(input)
    for _ in range(100):
        counts = {}
        for tile in tiles:
            for d in DIRECTIONS.values():
                counts[tile+d] = counts.get(tile+d, 0) + 1
        tiles = {t for t,n in counts.items() if n == 2 or (n == 1 and t in tiles)}
    return len(tiles)

def black(input):
    tiles = set()
    for line in input:
        tiles ^= {sum(DIRECTIONS[d] for d in re.findall(r"[ns]?[ew]", line))}
    return tiles

with open("2020/Day24_input.txt") as f:
    input = f.read().split()

    print(f"Part 1: {part_1(input)}")
    print(f"Part 2: {part_2(input)}")
