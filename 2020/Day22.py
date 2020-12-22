def score(deck):
    return sum(i*c for i,c in enumerate(reversed(deck), 1))

def combat(a, b, recursive):
    seen = set()
    while a and b:
        if (key := (tuple(a), tuple(b))) in seen:
            return True, a
        seen.add(key)
        x, y = a.pop(0), b.pop(0)
        if recursive and len(a) >= x and len(b) >= y:
            first = combat(a[:x], b[:y], True)[0]
        else:
            first = x > y
        (a if first else b).extend([x,y] if first else [y,x])
    return bool(a), a or b

def part_1(a, b):
    return score(combat(a[:], b[:], False)[1])

def part_2(a, b):
    return score(combat(a[:], b[:], True)[1])

with open("2020/Day22_input.txt") as f:
    a, b = ([int(x) for x in block.split()[2:]] for block in f.read().split("\n\n"))

    print(f"Part 1: {part_1(a, b)}")
    print(f"Part 2: {part_2(a, b)}")
