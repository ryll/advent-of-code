def group(input, start):
    seen, stack = {start}, [start]
    while stack:
        for n in input[stack.pop()]:
            if n not in seen:
                seen.add(n)
                stack.append(n)
    return seen

def part_1(input):
    return len(group(input, 0))

def part_2(input):
    remaining, groups = set(input), 0
    while remaining:
        remaining -= group(input, next(iter(remaining)))
        groups += 1
    return groups

with open("2017/Day12_input.txt") as f:
    input = {}
    for line in f.read().splitlines():
        program, neighbours = line.split(' <-> ')
        input[int(program)] = [int(v) for v in neighbours.split(', ')]

    print(f"Part 1: {part_1(input)}")
    print(f"Part 2: {part_2(input)}")
