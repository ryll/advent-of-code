import re
from math import prod

def mixtures(ingredients, spoons):
    if ingredients == 1:
        yield (spoons,)
    else:
        for n in range(spoons + 1):
            for rest in mixtures(ingredients - 1, spoons - n):
                yield (n,) + rest

def score(input, amounts, calories=None):
    if calories is not None and sum(n * ing[4] for n,ing in zip(amounts, input)) != calories:
        return 0
    return prod(max(0, sum(n * ing[i] for n,ing in zip(amounts, input))) for i in range(4))

def part_1(input):
    return max(score(input, amounts) for amounts in mixtures(len(input), 100))

def part_2(input):
    return max(score(input, amounts, 500) for amounts in mixtures(len(input), 100))

with open("2015/Day15_input.txt") as f:
    input = [[int(x) for x in re.findall(r'-?\d+', line)] for line in f.read().splitlines()]

    print(f"Part 1: {part_1(input)}")
    print(f"Part 2: {part_2(input)}")
