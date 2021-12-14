from collections import Counter

def polymerize(template, rules, steps):
    pairs = Counter(a+b for a,b in zip(template, template[1:]))
    for _ in range(steps):
        new = Counter()
        for pair,n in pairs.items():
            new[pair[0] + rules[pair]] += n
            new[rules[pair] + pair[1]] += n
        pairs = new
    counts = Counter(template[-1])
    for pair,n in pairs.items():
        counts[pair[0]] += n
    return max(counts.values()) - min(counts.values())

def part_1(template, rules):
    return polymerize(template, rules, 10)

def part_2(template, rules):
    return polymerize(template, rules, 40)

with open("2021/Day14_input.txt") as f:
    template, rule_block = f.read().split("\n\n")
    rules = dict(line.split(' -> ') for line in rule_block.split('\n') if line)

    print(f"Part 1: {part_1(template.strip(), rules)}")
    print(f"Part 2: {part_2(template.strip(), rules)}")
