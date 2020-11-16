from heapq import heappush, heappop

def erosion(depth, target):
    levels = {}
    for y in range(target[1] + 100):
        for x in range(target[0] + 100):
            if (x,y) in ((0,0), target):
                index = 0
            elif y == 0:
                index = x * 16807
            elif x == 0:
                index = y * 48271
            else:
                index = levels[(x-1,y)] * levels[(x,y-1)]
            levels[(x,y)] = (index + depth) % 20183
    return levels

def part_1(depth, target):
    levels = erosion(depth, target)
    return sum(levels[(x,y)] % 3 for x in range(target[0]+1) for y in range(target[1]+1))

def part_2(depth, target):
    levels = erosion(depth, target)
    goal, seen, queue = (*target, 1), set(), [(0, (0, 0, 1))]
    while queue:
        time, state = heappop(queue)
        if state == goal:
            return time
        if state in seen:
            continue
        seen.add(state)
        x, y, tool = state
        for other in range(3):
            if other != tool and other != levels[(x,y)] % 3:
                heappush(queue, (time + 7, (x, y, other)))
        for n in ((x-1,y), (x+1,y), (x,y-1), (x,y+1)):
            if n in levels and levels[n] % 3 != tool:
                heappush(queue, (time + 1, (*n, tool)))

with open("2018/Day22_input.txt") as f:
    depth_line, target_line = f.read().splitlines()
    depth = int(depth_line.split()[1])
    target = tuple(int(v) for v in target_line.split()[1].split(','))

    print(f"Part 1: {part_1(depth, target)}")
    print(f"Part 2: {part_2(depth, target)}")
