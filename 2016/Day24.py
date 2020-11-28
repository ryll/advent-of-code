from collections import deque
from itertools import permutations

def distances(ducts, start):
    queue, seen, found = deque([(start, 0)]), {start}, {}
    while queue:
        (x,y), steps = queue.popleft()
        if ducts[x,y].isdigit():
            found[int(ducts[x,y])] = steps
        for node in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
            if ducts.get(node, '#') != '#' and node not in seen:
                seen.add(node)
                queue.append((node, steps+1))
    return found

def shortest(ducts, points, home):
    table = {number: distances(ducts, node) for number,node in points.items()}
    return min(sum(table[a][b] for a,b in zip((0,) + order, order + ((0,) if home else ())))
               for order in permutations(number for number in points if number))

def part_1(ducts, points):
    return shortest(ducts, points, False)

def part_2(ducts, points):
    return shortest(ducts, points, True)

with open("2016/Day24_input.txt") as f:
    ducts = {(i,j): c for i,row in enumerate(f.read().split()) for j,c in enumerate(row)}
    points = {int(c): node for node,c in ducts.items() if c.isdigit()}

    print(f"Part 1: {part_1(ducts, points)}")
    print(f"Part 2: {part_2(ducts, points)}")
