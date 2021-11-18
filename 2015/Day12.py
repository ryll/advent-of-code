import json

def total(node, skip=None):
    if isinstance(node, int):
        return node
    if isinstance(node, list):
        return sum(total(child, skip) for child in node)
    if isinstance(node, dict):
        return 0 if skip in node.values() else sum(total(child, skip) for child in node.values())
    return 0

def part_1(input):
    return total(input)

def part_2(input):
    return total(input, 'red')

with open("2015/Day12_input.txt") as f:
    input = json.load(f)

    print(f"Part 1: {part_1(input)}")
    print(f"Part 2: {part_2(input)}")
