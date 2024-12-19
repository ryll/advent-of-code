from collections import deque

SIZE, FIRST = 71, 1024

def steps(corrupted):
    queue, seen = deque([((0,0), 0)]), {(0,0)}
    while queue:
        (x,y), d = queue.popleft()
        if (x,y) == (SIZE-1, SIZE-1):
            return d
        for p in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
            if all(0 <= v < SIZE for v in p) and p not in corrupted and p not in seen:
                seen.add(p)
                queue.append((p, d+1))

def part_1(falling):
    return steps(set(falling[:FIRST]))

def part_2(falling):
    lo, hi = FIRST, len(falling) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if steps(set(falling[:mid+1])) is None:
            hi = mid
        else:
            lo = mid + 1
    return ','.join(str(v) for v in falling[lo])

with open("2024/Day18_input.txt") as f:
    falling = [tuple(int(v) for v in line.split(',')) for line in f.read().split()]

    print(f"Part 1: {part_1(falling)}")
    print(f"Part 2: {part_2(falling)}")
