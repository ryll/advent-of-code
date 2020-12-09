def part_1(input, n=25):
    return next(x for i,x in enumerate(input[n:])
                if not any(x-a in input[i:i+n] for a in input[i:i+n] if 2*a != x))

def part_2(input):
    target = part_1(input)
    for i in range(len(input)):
        for j in range(i+2, len(input)):
            if sum(input[i:j]) == target:
                return min(input[i:j]) + max(input[i:j])

with open("2020/Day09_input.txt") as f:
    input = [int(x) for x in f.read().split()]

    print(f"Part 1: {part_1(input)}")
    print(f"Part 2: {part_2(input)}")
