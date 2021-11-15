OPS = {'AND': lambda a,b: a & b, 'OR': lambda a,b: a | b,
       'LSHIFT': lambda a,b: a << b, 'RSHIFT': lambda a,b: a >> b}

def solve(input, overrides={}):
    cache = dict(overrides)
    def value(wire):
        if wire.isdigit():
            return int(wire)
        if wire not in cache:
            parts = input[wire]
            if len(parts) == 1:
                cache[wire] = value(parts[0])
            elif len(parts) == 2:
                cache[wire] = ~value(parts[1]) & 0xFFFF
            else:
                cache[wire] = OPS[parts[1]](value(parts[0]), value(parts[2]))
        return cache[wire]
    return value('a')

def part_1(input):
    return solve(input)

def part_2(input):
    return solve(input, {'b': solve(input)})

with open("2015/Day07_input.txt") as f:
    input = {target: source.split() for source, target in
             (line.split(' -> ') for line in f.read().splitlines())}

    print(f"Part 1: {part_1(input)}")
    print(f"Part 2: {part_2(input)}")
