def part_1(input):
    return sum(len(set(phrase)) == len(phrase) for phrase in input)

def part_2(input):
    return sum(len({''.join(sorted(word)) for word in phrase}) == len(phrase)
               for phrase in input)

with open("2017/Day04_input.txt") as f:
    input = [line.split() for line in f.read().splitlines() if line]

    print(f"Part 1: {part_1(input)}")
    print(f"Part 2: {part_2(input)}")
