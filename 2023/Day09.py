def extrapolate(sequence):
    if not any(sequence):
        return 0
    return sequence[-1] + extrapolate([b-a for a,b in zip(sequence, sequence[1:])])

def part_1(input):
    return sum(extrapolate(sequence) for sequence in input)

def part_2(input):
    return sum(extrapolate(sequence[::-1]) for sequence in input)

with open("2023/Day09_input.txt") as f:
    input = [[int(v) for v in line.split()] for line in f.read().splitlines()]

    print(f"Part 1: {part_1(input)}")
    print(f"Part 2: {part_2(input)}")
