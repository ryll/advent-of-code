from itertools import cycle
from math import lcm

def steps(node, suffix, directions, network):
    for n,d in enumerate(cycle(directions), 1):
        node = network[node][d == 'R']
        if node.endswith(suffix):
            return n

def part_1(directions, network):
    return steps('AAA', 'ZZZ', directions, network)

def part_2(directions, network):
    return lcm(*(steps(node, 'Z', directions, network)
                 for node in network if node.endswith('A')))

with open("2023/Day08_input.txt") as f:
    direction_block, node_block = f.read().split("\n\n")
    directions = direction_block.strip()
    network = {line[0:3]: (line[7:10], line[12:15]) for line in node_block.splitlines()}

    print(f"Part 1: {part_1(directions, network)}")
    print(f"Part 2: {part_2(directions, network)}")
