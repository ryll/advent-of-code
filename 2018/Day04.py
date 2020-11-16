import re
from collections import Counter, defaultdict

def schedule(lines):
    minutes, guard, start = defaultdict(Counter), None, 0
    for line in lines:
        if 'Guard' in line:
            guard = int(re.search(r'#(\d+)', line).group(1))
        elif 'falls' in line:
            start = int(line[15:17])
        else:
            minutes[guard].update(range(start, int(line[15:17])))
    return minutes

def part_1(input):
    guard = max(input, key=lambda g: sum(input[g].values()))
    return guard * input[guard].most_common(1)[0][0]

def part_2(input):
    guard = max(input, key=lambda g: input[g].most_common(1)[0][1])
    return guard * input[guard].most_common(1)[0][0]

with open("2018/Day04_input.txt") as f:
    input = schedule(sorted(f.read().splitlines()))

    print(f"Part 1: {part_1(input)}")
    print(f"Part 2: {part_2(input)}")
