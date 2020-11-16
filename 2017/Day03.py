from itertools import count, islice

def spiral():
    x = y = 0
    yield (x, y)
    for ring in count(1):
        x += 1
        yield (x, y)
        while y < ring:
            y += 1
            yield (x, y)
        while x > -ring:
            x -= 1
            yield (x, y)
        while y > -ring:
            y -= 1
            yield (x, y)
        while x < ring:
            x += 1
            yield (x, y)

def part_1(input):
    x, y = next(islice(spiral(), input - 1, None))
    return abs(x) + abs(y)

def part_2(input):
    values = {(0,0): 1}
    for x,y in islice(spiral(), 1, None):
        values[(x,y)] = total = sum(values.get((x+dx, y+dy), 0)
                                    for dx in (-1,0,1) for dy in (-1,0,1))
        if total > input:
            return total

with open("2017/Day03_input.txt") as f:
    input = int(f.read().strip())

    print(f"Part 1: {part_1(input)}")
    print(f"Part 2: {part_2(input)}")
