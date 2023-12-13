def summarize(input, smudges):
    total = 0
    for pattern in input:
        rows = pattern.splitlines()
        for score,lines in ((100, rows), (1, [''.join(c) for c in zip(*rows)])):
            for i in range(1, len(lines)):
                if smudges == sum(a != b for above,below in zip(reversed(lines[:i]), lines[i:])
                                  for a,b in zip(above, below)):
                    total += score * i
    return total

def part_1(input):
    return summarize(input, 0)

def part_2(input):
    return summarize(input, 1)

with open("2023/Day13_input.txt") as f:
    input = f.read().split("\n\n")

    print(f"Part 1: {part_1(input)}")
    print(f"Part 2: {part_2(input)}")
