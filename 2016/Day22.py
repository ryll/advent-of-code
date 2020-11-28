import re
from collections import deque

def part_1(nodes):
    return sum(a != b and used and used <= nodes[b][0] - nodes[b][1]
               for a,(_,used) in nodes.items() for b in nodes)

def part_2(nodes):
    empty = next(node for node,(_,used) in nodes.items() if used == 0)
    goal = (max(x for x,_ in nodes), 0)
    start, target = (empty, goal), (0, 0)
    queue, seen = deque([(start, 0)]), {start}
    while queue:
        ((empty, goal), moved) = queue.popleft()
        if goal == target:
            return moved
        x, y = empty
        for node in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
            if node in nodes and nodes[node][1] <= nodes[empty][0]:
                state = (node, empty if node == goal else goal)
                if state not in seen:
                    seen.add(state)
                    queue.append((state, moved+1))

with open("2016/Day22_input.txt") as f:
    nodes = {}
    for line in f.read().splitlines():
        if line.startswith('/dev/grid'):
            x, y, size, used, _, _ = (int(v) for v in re.findall(r'\d+', line))
            nodes[x,y] = (size, used)

    print(f"Part 1: {part_1(nodes)}")
    print(f"Part 2: {part_2(nodes)}")
