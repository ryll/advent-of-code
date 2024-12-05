from functools import cmp_to_key

def order(update, rules):
    return sorted(update, key=cmp_to_key(lambda a,b: -1 if (a,b) in rules else 1))

def part_1(rules, updates):
    return sum(u[len(u)//2] for u in updates if order(u, rules) == u)

def part_2(rules, updates):
    return sum(s[len(s)//2] for u in updates if (s := order(u, rules)) != u)

with open("2024/Day05_input.txt") as f:
    rule_block, update_block = f.read().split("\n\n")
    rules = {tuple(int(v) for v in line.split('|')) for line in rule_block.split()}
    updates = [[int(v) for v in line.split(',')] for line in update_block.split()]

    print(f"Part 1: {part_1(rules, updates)}")
    print(f"Part 2: {part_2(rules, updates)}")
