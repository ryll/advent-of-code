from heapq import heappush, heappop

def distances(maze, start):
    dist, queue = {}, [(0, start, (0,1))]
    while queue:
        d, (i,j), (di,dj) = heappop(queue)
        if ((i,j), (di,dj)) in dist:
            continue
        dist[(i,j), (di,dj)] = d
        for cost,p,direction in ((d+1, (i+di, j+dj), (di,dj)),
                                 (d+1000, (i,j), (dj,-di)),
                                 (d+1000, (i,j), (-dj,di))):
            if maze.get(p) != '#' and (p, direction) not in dist:
                heappush(queue, (cost, p, direction))
    return dist

def best_score(maze, start, end):
    dist = distances(maze, start)
    return dist, min(d for (p,_),d in dist.items() if p == end)

def part_1(maze, start, end):
    return best_score(maze, start, end)[1]

def part_2(maze, start, end):
    dist, best = best_score(maze, start, end)
    stack = [state for state,d in dist.items() if state[0] == end and d == best]
    seen = set(stack)
    while stack:
        state = stack.pop()
        ((i,j), (di,dj)) = state
        for previous,cost in ((((i-di, j-dj), (di,dj)), 1),
                              (((i,j), (-dj,di)), 1000),
                              (((i,j), (dj,-di)), 1000)):
            if previous not in seen and dist.get(previous) == dist[state] - cost:
                seen.add(previous)
                stack.append(previous)
    return len({p for p,_ in seen})

with open("2024/Day16_input.txt") as f:
    maze = {(i,j): c for i,row in enumerate(f.read().split()) for j,c in enumerate(row)}
    start = next(p for p,c in maze.items() if c == 'S')
    end = next(p for p,c in maze.items() if c == 'E')

    print(f"Part 1: {part_1(maze, start, end)}")
    print(f"Part 2: {part_2(maze, start, end)}")
