from collections import deque
from math import prod

def min_cut(graph, source, target):
    residual = {u: dict.fromkeys(vs, 1) for u,vs in graph.items()}
    for flow in range(4):
        parents = {source: None}
        queue = deque([source])
        while queue and target not in parents:
            u = queue.popleft()
            for v,capacity in residual[u].items():
                if capacity and v not in parents:
                    parents[v] = u
                    queue.append(v)
        if target not in parents:
            return flow, len(parents)
        v = target
        while parents[v] is not None:
            residual[parents[v]][v] -= 1
            residual[v][parents[v]] += 1
            v = parents[v]
    return 4, 0

def part_1(graph):
    nodes = list(graph)
    for target in nodes[1:]:
        cut, size = min_cut(graph, nodes[0], target)
        if cut == 3:
            return size * (len(nodes) - size)

def part_2(graph):
    return "Merry Christmas!"

with open("2023/Day25_input.txt") as f:
    graph = {}
    for line in f.read().splitlines():
        name, others = line.split(': ')
        for other in others.split():
            graph.setdefault(name, set()).add(other)
            graph.setdefault(other, set()).add(name)

    print(f"Part 1: {part_1(graph)}")
    print(f"Part 2: {part_2(graph)}")
