def play(input, turns):
    seen = {n: i for i,n in enumerate(input[:-1], 1)}
    last = input[-1]
    for turn in range(len(input), turns):
        seen[last], last = turn, turn - seen.get(last, turn)
    return last

def part_1(input):
    return play(input, 2020)

def part_2(input):
    return play(input, 30000000)

with open("2020/Day15_input.txt") as f:
    input = [int(x) for x in f.read().split(',')]

    print(f"Part 1: {part_1(input)}")
    print(f"Part 2: {part_2(input)}")
