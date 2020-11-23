from collections import deque
from hashlib import md5

DOORS = (('U', 0, -1), ('D', 0, 1), ('L', -1, 0), ('R', 1, 0))

def paths(passcode):
    queue = deque([((0,0), '')])
    while queue:
        (x,y), path = queue.popleft()
        if (x,y) == (3,3):
            yield path
            continue
        digest = md5((passcode + path).encode()).hexdigest()
        for (door,dx,dy),state in zip(DOORS, digest):
            if state in 'bcdef' and 0 <= x+dx < 4 and 0 <= y+dy < 4:
                queue.append(((x+dx, y+dy), path + door))

def part_1(passcode):
    return next(paths(passcode))

def part_2(passcode):
    return max(len(path) for path in paths(passcode))

with open("2016/Day17_input.txt") as f:
    passcode = f.read().strip()

    print(f"Part 1: {part_1(passcode)}")
    print(f"Part 2: {part_2(passcode)}")
