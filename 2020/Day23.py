def play(input, size, moves):
    cups = list(input) + list(range(len(input)+1, size+1))
    next_cup = {c: cups[(i+1) % size] for i,c in enumerate(cups)}
    current = cups[0]
    for _ in range(moves):
        a = next_cup[current]
        b, c = next_cup[a], next_cup[next_cup[a]]
        next_cup[current] = next_cup[c]
        target = current - 1 or size
        while target in (a,b,c):
            target = target - 1 or size
        next_cup[c], next_cup[target] = next_cup[target], a
        current = next_cup[current]
    return next_cup

def part_1(input):
    next_cup, labels, cup = play(input, len(input), 100), '', 1
    for _ in range(len(input)-1):
        cup = next_cup[cup]
        labels += str(cup)
    return labels

def part_2(input):
    next_cup = play(input, 1000000, 10000000)
    return next_cup[1] * next_cup[next_cup[1]]

with open("2020/Day23_input.txt") as f:
    input = [int(c) for c in f.read().strip()]

    print(f"Part 1: {part_1(input)}")
    print(f"Part 2: {part_2(input)}")
