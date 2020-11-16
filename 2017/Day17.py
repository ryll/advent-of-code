def part_1(input):
    buffer, pos = [0], 0
    for i in range(1, 2018):
        pos = (pos + input) % i + 1
        buffer.insert(pos, i)
    return buffer[pos + 1]

def part_2(input):
    pos, after = 0, None
    for i in range(1, 50000001):
        pos = (pos + input) % i + 1
        if pos == 1:
            after = i
    return after

with open("2017/Day17_input.txt") as f:
    input = int(f.read().strip())

    print(f"Part 1: {part_1(input)}")
    print(f"Part 2: {part_2(input)}")
