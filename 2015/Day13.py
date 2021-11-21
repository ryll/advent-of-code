from itertools import permutations

def best(input, people):
    first, *rest = sorted(people)
    return max(sum(input.get((a,b), 0) + input.get((b,a), 0) for a,b in zip(table, table[1:]))
               for table in ((first,) + order + (first,) for order in permutations(rest)))

def part_1(input):
    return best(input, {p for pair in input for p in pair})

def part_2(input):
    return best(input, {p for pair in input for p in pair} | {'me'})

with open("2015/Day13_input.txt") as f:
    input = {}
    for line in f.read().splitlines():
        w = line.rstrip('.').split()
        input[w[0], w[-1]] = int(w[3]) * (1 if w[2] == 'gain' else -1)

    print(f"Part 1: {part_1(input)}")
    print(f"Part 2: {part_2(input)}")
