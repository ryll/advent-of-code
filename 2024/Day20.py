SAVING = 100

def cheats(path, limit):
    total = 0
    for k,(i1,j1) in enumerate(path):
        for l in range(k + SAVING, len(path)):
            i2, j2 = path[l]
            distance = abs(i1-i2) + abs(j1-j2)
            if distance <= limit and l - k - distance >= SAVING:
                total += 1
    return total

def part_1(path):
    return cheats(path, 2)

def part_2(path):
    return cheats(path, 20)

with open("2024/Day20_input.txt") as f:
    track = {(i,j): c for i,row in enumerate(f.read().split()) for j,c in enumerate(row) if c != '#'}
    path = [next(p for p,c in track.items() if c == 'S')]
    while track[path[-1]] != 'E':
        i, j = path[-1]
        path.append(next(p for p in ((i-1,j), (i+1,j), (i,j-1), (i,j+1))
                         if p in track and (len(path) == 1 or p != path[-2])))

    print(f"Part 1: {part_1(path)}")
    print(f"Part 2: {part_2(path)}")
