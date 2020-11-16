from collections import deque

def scoreboard():
    recipes, a, b = [3, 7], 0, 1
    yield from recipes
    while True:
        total = recipes[a] + recipes[b]
        for digit in (divmod(total, 10) if total >= 10 else (total,)):
            recipes.append(digit)
            yield digit
        a = (a + recipes[a] + 1) % len(recipes)
        b = (b + recipes[b] + 1) % len(recipes)

def part_1(input):
    scores = scoreboard()
    return ''.join(str(next(scores)) for _ in range(int(input) + 10))[-10:]

def part_2(input):
    target = deque(int(c) for c in input)
    window = deque(maxlen=len(target))
    for i,digit in enumerate(scoreboard()):
        window.append(digit)
        if window == target:
            return i + 1 - len(target)

with open("2018/Day14_input.txt") as f:
    input = f.read().strip()

    print(f"Part 1: {part_1(input)}")
    print(f"Part 2: {part_2(input)}")
