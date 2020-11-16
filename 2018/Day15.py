from collections import deque
from itertools import count

def neighbours(p):
    y, x = p
    return ((y-1,x), (y,x-1), (y,x+1), (y+1,x))

def distances(walls, occupied, start):
    dist, queue = {start: 0}, deque([start])
    while queue:
        p = queue.popleft()
        for n in neighbours(p):
            if n not in dist and n not in walls and n not in occupied:
                dist[n] = dist[p] + 1
                queue.append(n)
    return dist

def step(walls, occupied, pos, in_range):
    forward = distances(walls, occupied, pos)
    reachable = [(d, p) for p,d in forward.items() if p in in_range]
    if not reachable:
        return pos
    backward = distances(walls, occupied, min(reachable)[1])
    return min((backward[n], n) for n in neighbours(pos) if n in backward)[1]

def battle(walls, start, power):
    units = {p: [kind, 200] for p,kind in start.items()}
    for rounds in count():
        for pos in sorted(units):
            if pos not in units:
                continue
            kind = units[pos][0]
            enemies = {p for p,(k,_) in units.items() if k != kind}
            if not enemies:
                return rounds * sum(hp for _,hp in units.values()), units
            if not any(n in enemies for n in neighbours(pos)):
                moved = step(walls, set(units) - {pos}, pos,
                             {n for e in enemies for n in neighbours(e)} - walls - set(units))
                if moved != pos:
                    units[moved] = units.pop(pos)
                    pos = moved
            if targets := sorted((units[n][1], n) for n in neighbours(pos) if n in enemies):
                target = targets[0][1]
                units[target][1] -= power if kind == 'E' else 3
                if units[target][1] <= 0:
                    del units[target]

def part_1(walls, units):
    return battle(walls, units, 3)[0]

def part_2(walls, units):
    elves = sum(kind == 'E' for kind in units.values())
    for power in count(4):
        outcome, survivors = battle(walls, units, power)
        if sum(kind == 'E' for kind,_ in survivors.values()) == elves:
            return outcome

with open("2018/Day15_input.txt") as f:
    walls, units = set(), {}
    for y,row in enumerate(f.read().splitlines()):
        for x,c in enumerate(row):
            if c == '#':
                walls.add((y,x))
            elif c in 'EG':
                units[(y,x)] = c

    print(f"Part 1: {part_1(walls, units)}")
    print(f"Part 2: {part_2(walls, units)}")
