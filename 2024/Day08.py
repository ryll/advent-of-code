from itertools import combinations

def antinodes(antennas, rows, cols, harmonics):
    found = set()
    for positions in antennas.values():
        for (i1,j1),(i2,j2) in combinations(positions, 2):
            di, dj = i2-i1, j2-j1
            for i,j,s in ((i1,j1,-1), (i2,j2,1)):
                if not harmonics:
                    i, j = i+s*di, j+s*dj
                while 0 <= i < rows and 0 <= j < cols:
                    found.add((i,j))
                    if not harmonics:
                        break
                    i, j = i+s*di, j+s*dj
    return len(found)

def part_1(antennas, rows, cols):
    return antinodes(antennas, rows, cols, False)

def part_2(antennas, rows, cols):
    return antinodes(antennas, rows, cols, True)

with open("2024/Day08_input.txt") as f:
    lines = f.read().split()
    rows, cols = len(lines), len(lines[0])
    antennas = {}
    for i,row in enumerate(lines):
        for j,c in enumerate(row):
            if c != '.':
                antennas.setdefault(c, []).append((i,j))

    print(f"Part 1: {part_1(antennas, rows, cols)}")
    print(f"Part 2: {part_2(antennas, rows, cols)}")
