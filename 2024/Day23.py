from itertools import combinations

def part_1(network):
    return len({tuple(sorted((a,b,c))) for a in network if a.startswith('t')
                for b,c in combinations(network[a], 2) if c in network[b]})

def part_2(network):
    best = set()
    def grow(clique, candidates):
        nonlocal best
        if len(clique) + len(candidates) <= len(best):
            return
        if not candidates:
            best = set(clique)
            return
        for computer in list(candidates):
            grow(clique | {computer}, candidates & network[computer])
            candidates = candidates - {computer}
    grow(set(), set(network))
    return ','.join(sorted(best))

with open("2024/Day23_input.txt") as f:
    network = {}
    for line in f.read().split():
        a, b = line.split('-')
        network.setdefault(a, set()).add(b)
        network.setdefault(b, set()).add(a)

    print(f"Part 1: {part_1(network)}")
    print(f"Part 2: {part_2(network)}")
