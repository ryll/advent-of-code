from functools import cache

@cache
def arrangements(springs, groups):
    if not groups:
        return '#' not in springs
    if len(springs) < sum(groups) + len(groups) - 1:
        return 0
    n, total = groups[0], 0
    if springs[0] != '#':
        total += arrangements(springs[1:], groups)
    if '.' not in springs[:n] and (len(springs) == n or springs[n] != '#'):
        total += arrangements(springs[n+1:], groups[1:])
    return total

def part_1(input):
    return sum(arrangements(springs, groups) for springs,groups in input)

def part_2(input):
    return sum(arrangements('?'.join([springs]*5), groups*5) for springs,groups in input)

with open("2023/Day12_input.txt") as f:
    input = [(springs, tuple(int(v) for v in groups.split(',')))
             for springs,groups in (line.split() for line in f.read().splitlines())]

    print(f"Part 1: {part_1(input)}")
    print(f"Part 2: {part_2(input)}")
