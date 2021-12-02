def part_1(input):
    pos = depth = 0
    for command,value in input:
        pos += value * (command == 'forward')
        depth += value * ((command == 'down') - (command == 'up'))
    return pos * depth

def part_2(input):
    pos = depth = aim = 0
    for command,value in input:
        aim += value * ((command == 'down') - (command == 'up'))
        pos += value * (command == 'forward')
        depth += aim * value * (command == 'forward')
    return pos * depth

with open("2021/Day02_input.txt") as f:
    input = [(c, int(v)) for c,v in (line.split() for line in f)]

    print(f"Part 1: {part_1(input)}")
    print(f"Part 2: {part_2(input)}")
