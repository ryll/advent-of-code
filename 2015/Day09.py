from itertools import permutations

def routes(input):
    places = {p for pair in input for p in pair}
    return [sum(input[a,b] for a,b in zip(route, route[1:])) for route in permutations(places)]

def part_1(input):
    return min(routes(input))

def part_2(input):
    return max(routes(input))

with open("2015/Day09_input.txt") as f:
    input = {}
    for line in f.read().splitlines():
        route, dist = line.split(' = ')
        a, b = route.split(' to ')
        input[a,b] = input[b,a] = int(dist)

    print(f"Part 1: {part_1(input)}")
    print(f"Part 2: {part_2(input)}")
