def escape(input, strange):
    jumps, i, steps = list(input), 0, 0
    while 0 <= i < len(jumps):
        offset = jumps[i]
        jumps[i] += -1 if strange and offset >= 3 else 1
        i += offset
        steps += 1
    return steps

def part_1(input):
    return escape(input, False)

def part_2(input):
    return escape(input, True)

with open("2017/Day05_input.txt") as f:
    input = [int(v) for v in f.read().split()]

    print(f"Part 1: {part_1(input)}")
    print(f"Part 2: {part_2(input)}")
