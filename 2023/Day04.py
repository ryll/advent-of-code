def matches(card):
    winning, have = card
    return len(winning & have)

def part_1(input):
    return sum(2**(m-1) for card in input if (m := matches(card)))

def part_2(input):
    counts = [1] * len(input)
    for i,card in enumerate(input):
        for j in range(i+1, min(i+1+matches(card), len(input))):
            counts[j] += counts[i]
    return sum(counts)

with open("2023/Day04_input.txt") as f:
    input = [tuple({int(v) for v in half.split()} for half in line.split(': ')[1].split(' | '))
             for line in f.read().splitlines()]

    print(f"Part 1: {part_1(input)}")
    print(f"Part 2: {part_2(input)}")
