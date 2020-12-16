def part_1(rules, mine, nearby):
    valid = {v for ranges in rules.values() for lo,hi in ranges for v in range(lo, hi+1)}
    return sum(v for ticket in nearby for v in ticket if v not in valid)

def part_2(rules, mine, nearby):
    valid = {v for ranges in rules.values() for lo,hi in ranges for v in range(lo, hi+1)}
    tickets = [t for t in nearby if all(v in valid for v in t)]
    options = {i: {name for name,ranges in rules.items()
                   if all(any(lo <= t[i] <= hi for lo,hi in ranges) for t in tickets)}
               for i in range(len(mine))}
    answer = 1
    while options:
        i = min(options, key=lambda i: len(options[i]))
        name = options.pop(i).pop()
        answer *= mine[i] if name.startswith('departure') else 1
        for rest in options.values():
            rest.discard(name)
    return answer

with open("2020/Day16_input.txt") as f:
    rule_block, mine, nearby = f.read().split("\n\n")
    rules = {}
    for line in rule_block.splitlines():
        name, ranges = line.split(': ')
        rules[name] = [tuple(map(int, r.split('-'))) for r in ranges.split(' or ')]
    mine = [int(x) for x in mine.splitlines()[1].split(',')]
    nearby = [[int(x) for x in line.split(',')] for line in nearby.splitlines()[1:]]

    print(f"Part 1: {part_1(rules, mine, nearby)}")
    print(f"Part 2: {part_2(rules, mine, nearby)}")
