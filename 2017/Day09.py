def process(input):
    stream = iter(input)
    score = depth = garbage = 0
    for c in stream:
        if c == '<':
            for g in stream:
                if g == '!':
                    next(stream, None)
                elif g == '>':
                    break
                else:
                    garbage += 1
        elif c == '{':
            depth += 1
            score += depth
        elif c == '}':
            depth -= 1
    return score, garbage

def part_1(input):
    return process(input)[0]

def part_2(input):
    return process(input)[1]

with open("2017/Day09_input.txt") as f:
    input = f.read().strip()

    print(f"Part 1: {part_1(input)}")
    print(f"Part 2: {part_2(input)}")
