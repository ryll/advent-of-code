from collections import Counter
from functools import cache
from itertools import product

ROLLS = Counter(sum(r) for r in product((1,2,3), repeat=3))

def part_1(input):
    positions, scores, die = list(input), [0,0], 0
    for turn in range(10**6):
        player = turn % 2
        positions[player] = (positions[player] + 3*die + 6) % 10 or 10
        scores[player] += positions[player]
        die += 3
        if scores[player] >= 1000:
            return scores[1-player] * die

@cache
def wins(a, b, score_a, score_b):
    total = [0, 0]
    for roll,n in ROLLS.items():
        pos = (a + roll) % 10 or 10
        if score_a + pos >= 21:
            total[0] += n
        else:
            second, first = wins(b, pos, score_b, score_a + pos)
            total[0] += n * first
            total[1] += n * second
    return tuple(total)

def part_2(input):
    return max(wins(*input, 0, 0))

with open("2021/Day21_input.txt") as f:
    input = tuple(int(line.split(': ')[1]) for line in f.read().splitlines())

    print(f"Part 1: {part_1(input)}")
    print(f"Part 2: {part_2(input)}")
