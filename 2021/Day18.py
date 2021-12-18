from itertools import permutations

def parse(line):
    depth, number = 0, []
    for c in line:
        depth += (c == '[') - (c == ']')
        if c.isdigit():
            number.append([int(c), depth])
    return number

def reduce(number):
    while True:
        for i,(value,depth) in enumerate(number):
            if depth > 4:
                if i:
                    number[i-1][0] += value
                if i+2 < len(number):
                    number[i+2][0] += number[i+1][0]
                number[i:i+2] = [[0, depth-1]]
                break
        else:
            for i,(value,depth) in enumerate(number):
                if value > 9:
                    number[i:i+1] = [[value//2, depth+1], [(value+1)//2, depth+1]]
                    break
            else:
                return number

def magnitude(number):
    number = [list(p) for p in number]
    while len(number) > 1:
        depth = max(d for _,d in number)
        i = next(i for i,(_,d) in enumerate(number) if d == depth)
        number[i:i+2] = [[3*number[i][0] + 2*number[i+1][0], depth-1]]
    return number[0][0]

def add(a, b):
    return reduce([[v, d+1] for v,d in a+b])

def part_1(input):
    total = input[0]
    for number in input[1:]:
        total = add(total, number)
    return magnitude(total)

def part_2(input):
    return max(magnitude(add([list(p) for p in a], [list(p) for p in b]))
               for a,b in permutations(input, 2))

with open("2021/Day18_input.txt") as f:
    input = [parse(line) for line in f.read().split()]

    print(f"Part 1: {part_1([[list(p) for p in n] for n in input])}")
    print(f"Part 2: {part_2(input)}")
