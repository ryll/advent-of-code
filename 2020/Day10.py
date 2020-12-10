def part_1(input):
    diffs = [b-a for a,b in zip(input, input[1:])]
    return diffs.count(1) * diffs.count(3)

def part_2(input):
    ways = {0: 1}
    for j in input[1:]:
        ways[j] = ways.get(j-1,0) + ways.get(j-2,0) + ways.get(j-3,0)
    return ways[input[-1]]

with open("2020/Day10_input.txt") as f:
    input = sorted(int(x) for x in f.read().split())
    input = [0] + input + [input[-1]+3]

    print(f"Part 1: {part_1(input)}")
    print(f"Part 2: {part_2(input)}")
