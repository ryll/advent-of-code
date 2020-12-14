def part_1(input):
    pos, dir = 0j, 1+0j
    for action,value in input:
        if action == 'F':   pos += dir * value
        elif action == 'L': dir *= 1j ** (value // 90)
        elif action == 'R': dir *= (-1j) ** (value // 90)
        else:               pos += {'N':1j, 'S':-1j, 'E':1, 'W':-1}[action] * value
    return int(abs(pos.real) + abs(pos.imag))

def part_2(input):
    pos, way = 0j, 10+1j
    for action,value in input:
        if action == 'F':   pos += way * value
        elif action == 'L': way *= 1j ** (value // 90)
        elif action == 'R': way *= (-1j) ** (value // 90)
        else:               way += {'N':1j, 'S':-1j, 'E':1, 'W':-1}[action] * value
    return int(abs(pos.real) + abs(pos.imag))

with open("2020/Day12_input.txt") as f:
    input = [(line[0], int(line[1:])) for line in f.read().split()]

    print(f"Part 1: {part_1(input)}")
    print(f"Part 2: {part_2(input)}")
