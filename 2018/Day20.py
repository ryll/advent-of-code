MOVES = {'N': (-1,0), 'S': (1,0), 'E': (0,1), 'W': (0,-1)}

def distances(regex):
    dist, stack, pos = {(0,0): 0}, [], (0,0)
    for c in regex:
        if c == '(':
            stack.append(pos)
        elif c == '|':
            pos = stack[-1]
        elif c == ')':
            pos = stack.pop()
        elif c in MOVES:
            dy, dx = MOVES[c]
            room = (pos[0] + dy, pos[1] + dx)
            dist[room] = min(dist.get(room, dist[pos] + 1), dist[pos] + 1)
            pos = room
    return dist

def part_1(input):
    return max(distances(input).values())

def part_2(input):
    return sum(d >= 1000 for d in distances(input).values())

with open("2018/Day20_input.txt") as f:
    input = f.read().strip()

    print(f"Part 1: {part_1(input)}")
    print(f"Part 2: {part_2(input)}")
