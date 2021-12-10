PAIRS = {'(':')', '[':']', '{':'}', '<':'>'}
ERROR = {')':3, ']':57, '}':1197, '>':25137}

def check(line):
    stack = []
    for c in line:
        if c in PAIRS:
            stack.append(PAIRS[c])
        elif c != stack.pop():
            return c, None
    return None, stack

def part_1(input):
    return sum(ERROR[c] for c,_ in map(check, input) if c)

def part_2(input):
    scores = []
    for bad,stack in map(check, input):
        if not bad:
            score = 0
            for c in reversed(stack):
                score = score * 5 + ' )]}>'.index(c)
            scores.append(score)
    return sorted(scores)[len(scores)//2]

with open("2021/Day10_input.txt") as f:
    input = f.read().split()

    print(f"Part 1: {part_1(input)}")
    print(f"Part 2: {part_2(input)}")
