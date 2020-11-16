import re
from collections import Counter

def weigh(input, name, answer):
    weight, children = input[name]
    totals = [weigh(input, child, answer) for child in children]
    counts = Counter(totals)
    if len(counts) > 1:
        odd, = (t for t in counts if counts[t] == 1)
        common, = (t for t in counts if counts[t] > 1)
        answer.append(input[children[totals.index(odd)]][0] + common - odd)
    return weight + sum(totals)

def part_1(input):
    return (set(input) - {c for _,children in input.values() for c in children}).pop()

def part_2(input):
    answer = []
    weigh(input, part_1(input), answer)
    return answer[0]

with open("2017/Day07_input.txt") as f:
    input = {}
    for line in f.read().splitlines():
        name, weight, *children = re.findall(r'\w+', line)
        input[name] = (int(weight), children)

    print(f"Part 1: {part_1(input)}")
    print(f"Part 2: {part_2(input)}")
