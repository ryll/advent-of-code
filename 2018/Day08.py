def read(numbers):
    children, metadata = next(numbers), next(numbers)
    return ([read(numbers) for _ in range(children)],
            [next(numbers) for _ in range(metadata)])

def total(node):
    children, metadata = node
    return sum(metadata) + sum(total(c) for c in children)

def value(node):
    children, metadata = node
    if not children:
        return sum(metadata)
    return sum(value(children[m-1]) for m in metadata if 1 <= m <= len(children))

def part_1(input):
    return total(input)

def part_2(input):
    return value(input)

with open("2018/Day08_input.txt") as f:
    input = read(iter([int(x) for x in f.read().split()]))

    print(f"Part 1: {part_1(input)}")
    print(f"Part 2: {part_2(input)}")
