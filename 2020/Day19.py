import re

def build(rules, key, depth=0):
    rule = rules[key]
    if rule.startswith('"'):
        return rule.strip('"')
    if depth > 20:
        return '$^'
    options = [''.join(build(rules, k, depth+1) for k in option.split()) for option in rule.split(' | ')]
    return '(?:' + '|'.join(options) + ')'

def part_1(rules, messages):
    pattern = re.compile(build(rules, '0'))
    return sum(bool(pattern.fullmatch(m)) for m in messages)

def part_2(rules, messages):
    return part_1(rules | {'8': '42 | 42 8', '11': '42 31 | 42 11 31'}, messages)

with open("2020/Day19_input.txt") as f:
    rule_block, message_block = f.read().split("\n\n")
    rules = dict(line.split(': ') for line in rule_block.splitlines())
    messages = message_block.split()

    print(f"Part 1: {part_1(rules, messages)}")
    print(f"Part 2: {part_2(rules, messages)}")
