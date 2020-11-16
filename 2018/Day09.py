import re
from collections import deque

def play(players, last):
    circle, scores = deque([0]), [0] * players
    for marble in range(1, last+1):
        if marble % 23:
            circle.rotate(-1)
            circle.append(marble)
        else:
            circle.rotate(7)
            scores[marble % players] += marble + circle.pop()
            circle.rotate(-1)
    return max(scores)

def part_1(players, last):
    return play(players, last)

def part_2(players, last):
    return play(players, last * 100)

with open("2018/Day09_input.txt") as f:
    players, last = (int(v) for v in re.findall(r'\d+', f.read()))

    print(f"Part 1: {part_1(players, last)}")
    print(f"Part 2: {part_2(players, last)}")
