def step(on, size, stuck):
    new = set()
    for i in range(size):
        for j in range(size):
            lit = sum((i+di, j+dj) in on for di in (-1,0,1) for dj in (-1,0,1) if (di,dj) != (0,0))
            if lit == 3 or (lit == 2 and (i,j) in on):
                new.add((i,j))
    return new | stuck

def animate(input, size, steps, stuck):
    on = input | stuck
    for _ in range(steps):
        on = step(on, size, stuck)
    return len(on)

def part_1(input, size=100):
    return animate(input, size, 100, set())

def part_2(input, size=100):
    last = size - 1
    return animate(input, size, 100, {(0,0), (0,last), (last,0), (last,last)})

with open("2015/Day18_input.txt") as f:
    input = {(i,j) for i,row in enumerate(f.read().split()) for j,c in enumerate(row) if c == '#'}

    print(f"Part 1: {part_1(input)}")
    print(f"Part 2: {part_2(input)}")
