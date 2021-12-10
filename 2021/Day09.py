from math import prod

def neighbours(i, j):
    return [(i-1,j), (i+1,j), (i,j-1), (i,j+1)]

def lows(input):
    return [p for p,h in input.items() if all(h < input.get(n, 9) for n in neighbours(*p))]

def part_1(input):
    return sum(input[p] + 1 for p in lows(input))

def part_2(input):
    sizes = []
    for low in lows(input):
        basin, stack = {low}, [low]
        while stack:
            for n in neighbours(*stack.pop()):
                if n not in basin and input.get(n, 9) < 9:
                    basin.add(n)
                    stack.append(n)
        sizes.append(len(basin))
    return prod(sorted(sizes)[-3:])

with open("2021/Day09_input.txt") as f:
    input = {(i,j): int(c) for i,row in enumerate(f.read().split()) for j,c in enumerate(row)}

    print(f"Part 1: {part_1(input)}")
    print(f"Part 2: {part_2(input)}")
