def distance(deer, seconds):
    speed, fly, rest = deer
    cycles, partial = divmod(seconds, fly + rest)
    return speed * (cycles * fly + min(partial, fly))

def part_1(input, seconds=2503):
    return max(distance(deer, seconds) for deer in input.values())

def part_2(input, seconds=2503):
    points = dict.fromkeys(input, 0)
    for t in range(1, seconds + 1):
        lead = max(distance(deer, t) for deer in input.values())
        for name, deer in input.items():
            if distance(deer, t) == lead:
                points[name] += 1
    return max(points.values())

with open("2015/Day14_input.txt") as f:
    input = {w[0]: (int(w[3]), int(w[6]), int(w[13]))
             for w in (line.split() for line in f.read().splitlines())}

    print(f"Part 1: {part_1(input)}")
    print(f"Part 2: {part_2(input)}")
