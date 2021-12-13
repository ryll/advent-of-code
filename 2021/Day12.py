def paths(caves, cave, visited, twice):
    if cave == 'end':
        return 1
    total = 0
    for next_cave in caves[cave]:
        if next_cave.isupper() or next_cave not in visited:
            total += paths(caves, next_cave, visited | {next_cave}, twice)
        elif twice and next_cave != 'start':
            total += paths(caves, next_cave, visited, False)
    return total

def part_1(input):
    return paths(input, 'start', {'start'}, False)

def part_2(input):
    return paths(input, 'start', {'start'}, True)

with open("2021/Day12_input.txt") as f:
    input = {}
    for line in f.read().split():
        a, b = line.split('-')
        input.setdefault(a, []).append(b)
        input.setdefault(b, []).append(a)

    print(f"Part 1: {part_1(input)}")
    print(f"Part 2: {part_2(input)}")
