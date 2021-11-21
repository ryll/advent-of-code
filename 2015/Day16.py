TARGET = {'children': 3, 'cats': 7, 'samoyeds': 2, 'pomeranians': 3, 'akitas': 0,
          'vizslas': 0, 'goldfish': 5, 'trees': 3, 'cars': 2, 'perfumes': 1}

def part_1(input):
    return next(sue for sue,props in input.items() if all(TARGET[k] == v for k,v in props.items()))

def part_2(input):
    def matches(k, v):
        if k in ('cats', 'trees'):
            return v > TARGET[k]
        if k in ('pomeranians', 'goldfish'):
            return v < TARGET[k]
        return v == TARGET[k]
    return next(sue for sue,props in input.items() if all(matches(k, v) for k,v in props.items()))

with open("2015/Day16_input.txt") as f:
    input = {}
    for line in f.read().splitlines():
        sue, props = line.split(': ', 1)
        input[int(sue.split()[1])] = {k: int(v) for k,v in (p.split(': ') for p in props.split(', '))}

    print(f"Part 1: {part_1(input)}")
    print(f"Part 2: {part_2(input)}")
