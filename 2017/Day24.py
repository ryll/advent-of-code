def bridges(input, port, used, strength, length):
    yield strength, length
    for i,(a,b) in enumerate(input):
        if i not in used and port in (a, b):
            yield from bridges(input, b if port == a else a, used | {i},
                               strength + a + b, length + 1)

def part_1(input):
    return max(strength for strength,_ in bridges(input, 0, frozenset(), 0, 0))

def part_2(input):
    return max((length, strength) for strength,length in bridges(input, 0, frozenset(), 0, 0))[1]

with open("2017/Day24_input.txt") as f:
    input = [tuple(int(v) for v in line.split('/')) for line in f.read().split()]

    print(f"Part 1: {part_1(input)}")
    print(f"Part 2: {part_2(input)}")
