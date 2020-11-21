from collections import deque
from itertools import takewhile

TARGET = (31, 39)

def reachable(favourite):
    queue, seen = deque([((1,1), 0)]), {(1,1)}
    while queue:
        (x,y), distance = queue.popleft()
        yield (x,y), distance
        for a,b in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
            if min(a,b) >= 0 and (a,b) not in seen \
                    and bin(a*a + 3*a + 2*a*b + b + b*b + favourite).count('1') % 2 == 0:
                seen.add((a,b))
                queue.append(((a,b), distance+1))

def part_1(favourite):
    return next(distance for room,distance in reachable(favourite) if room == TARGET)

def part_2(favourite):
    return sum(1 for _ in takewhile(lambda r: r[1] <= 50, reachable(favourite)))

with open("2016/Day13_input.txt") as f:
    favourite = int(f.read())

    print(f"Part 1: {part_1(favourite)}")
    print(f"Part 2: {part_2(favourite)}")
