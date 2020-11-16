def part_1(input):
    parent = list(range(len(input)))

    def find(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i

    for i,a in enumerate(input):
        for j,b in enumerate(input[:i]):
            if sum(abs(x-y) for x,y in zip(a,b)) <= 3:
                parent[find(i)] = find(j)
    return len({find(i) for i in range(len(input))})

def part_2(input):
    return "Merry Christmas!"

with open("2018/Day25_input.txt") as f:
    input = [tuple(int(v) for v in line.split(',')) for line in f.read().split()]

    print(f"Part 1: {part_1(input)}")
    print(f"Part 2: {part_2(input)}")
