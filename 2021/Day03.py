def part_1(input):
    gamma = ''.join(max('01', key=col.count) for col in zip(*input))
    return int(gamma, 2) * int(gamma.translate(str.maketrans('01','10')), 2)

def filter_by(input, keep):
    for i in range(len(input[0])):
        if len(input) == 1:
            break
        col = [line[i] for line in input]
        wanted = keep(col.count('1') >= col.count('0'))
        input = [line for line in input if line[i] == wanted]
    return int(input[0], 2)

def part_2(input):
    return filter_by(input, lambda most: '1' if most else '0') * filter_by(input, lambda most: '0' if most else '1')

with open("2021/Day03_input.txt") as f:
    input = f.read().split()

    print(f"Part 1: {part_1(input)}")
    print(f"Part 2: {part_2(input)}")
