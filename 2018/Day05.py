def react(polymer):
    stack = []
    for unit in polymer:
        if stack and stack[-1] != unit and stack[-1].lower() == unit.lower():
            stack.pop()
        else:
            stack.append(unit)
    return len(stack)

def part_1(input):
    return react(input)

def part_2(input):
    return min(react([c for c in input if c.lower() != u]) for u in set(input.lower()))

with open("2018/Day05_input.txt") as f:
    input = f.read().strip()

    print(f"Part 1: {part_1(input)}")
    print(f"Part 2: {part_2(input)}")
