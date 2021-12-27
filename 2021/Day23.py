from heapq import heappush, heappop

TYPES = 'ABCD'
COST = {'A':1, 'B':10, 'C':100, 'D':1000}
STOPS = (0, 1, 3, 5, 7, 9, 10)
EXTRA = ('DD', 'CB', 'BA', 'AC')

def clear(hall, a, b):
    return all(hall[k] == '.' for k in range(min(a,b), max(a,b)+1) if k != a)

def moves(hall, rooms):
    for j,room in enumerate(rooms):
        entrance = 2 + 2*j
        if all(c in ('.', TYPES[j]) for c in room):
            continue
        d = next(i for i,c in enumerate(room) if c != '.')
        for stop in STOPS:
            if clear(hall, stop, entrance) and hall[stop] == '.':
                yield (COST[room[d]] * (d + 1 + abs(stop - entrance)),
                       hall[:stop] + room[d] + hall[stop+1:],
                       rooms[:j] + (room[:d] + '.' + room[d+1:],) + rooms[j+1:])
    for i,c in enumerate(hall):
        if c == '.':
            continue
        j = TYPES.index(c)
        room, entrance = rooms[j], 2 + 2*TYPES.index(c)
        if any(x not in ('.', c) for x in room) or not clear(hall, i, entrance):
            continue
        d = room.count('.') - 1
        yield (COST[c] * (d + 1 + abs(i - entrance)),
               hall[:i] + '.' + hall[i+1:],
               rooms[:j] + (room[:d] + c + room[d+1:],) + rooms[j+1:])

def solve(rooms):
    goal = tuple(t * len(rooms[0]) for t in TYPES)
    seen, queue = set(), [(0, '.'*11, tuple(rooms))]
    while queue:
        energy, hall, state = heappop(queue)
        if state == goal:
            return energy
        if (hall, state) in seen:
            continue
        seen.add((hall, state))
        for cost,new_hall,new_state in moves(hall, state):
            heappush(queue, (energy + cost, new_hall, new_state))

def part_1(input):
    return solve(input)

def part_2(input):
    return solve([room[0] + EXTRA[j] + room[1:] for j,room in enumerate(input)])

with open("2021/Day23_input.txt") as f:
    rows = [[c for c in line if c in TYPES] for line in f.read().splitlines()]
    input = [''.join(row[j] for row in rows if row) for j in range(4)]

    print(f"Part 1: {part_1(input)}")
    print(f"Part 2: {part_2(input)}")
