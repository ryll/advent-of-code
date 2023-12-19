import re
from math import prod

def part_1(workflows, parts):
    total = 0
    for part in parts:
        name = 'in'
        while name not in ('A', 'R'):
            for condition,target in workflows[name]:
                if condition is None:
                    name = target
                    break
                key, op, value = condition
                if (part[key] < value) if op == '<' else (part[key] > value):
                    name = target
                    break
        total += sum(part.values()) if name == 'A' else 0
    return total

def combinations(workflows, name, ranges):
    if name == 'R':
        return 0
    if name == 'A':
        return prod(hi - lo for lo,hi in ranges.values())
    total = 0
    for condition,target in workflows[name]:
        if condition is None:
            return total + combinations(workflows, target, ranges)
        key, op, value = condition
        lo, hi = ranges[key]
        taken, rest = ((lo, min(hi, value)), (max(lo, value), hi)) if op == '<' else \
                      ((max(lo, value+1), hi), (lo, min(hi, value+1)))
        if taken[0] < taken[1]:
            total += combinations(workflows, target, {**ranges, key: taken})
        if rest[0] >= rest[1]:
            break
        ranges = {**ranges, key: rest}
    return total

def part_2(workflows, parts):
    return combinations(workflows, 'in', dict.fromkeys('xmas', (1, 4001)))

with open("2023/Day19_input.txt") as f:
    workflow_block, part_block = f.read().split("\n\n")
    workflows = {}
    for line in workflow_block.splitlines():
        name, body = line[:-1].split('{')
        rules = []
        for rule in body.split(','):
            if ':' in rule:
                condition, target = rule.split(':')
                rules.append(((condition[0], condition[1], int(condition[2:])), target))
            else:
                rules.append((None, rule))
        workflows[name] = rules
    parts = [{k: int(v) for k,v in re.findall(r"(\w)=(\d+)", line)}
             for line in part_block.splitlines()]

    print(f"Part 1: {part_1(workflows, parts)}")
    print(f"Part 2: {part_2(workflows, parts)}")
