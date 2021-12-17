from math import prod

def parse(bits, i):
    version, type_id = int(bits[i:i+3], 2), int(bits[i+3:i+6], 2)
    i += 6
    if type_id == 4:
        value = ''
        while bits[i] == '1':
            value += bits[i+1:i+5]
            i += 5
        return version, int(value + bits[i+1:i+5], 2), i+5
    versions, values = version, []
    if bits[i] == '0':
        end = i + 16 + int(bits[i+1:i+16], 2)
        i += 16
        while i < end:
            v, value, i = parse(bits, i)
            versions += v
            values.append(value)
    else:
        count = int(bits[i+1:i+12], 2)
        i += 12
        for _ in range(count):
            v, value, i = parse(bits, i)
            versions += v
            values.append(value)
    value = [sum, prod, min, max, None, lambda v: v[0] > v[1],
             lambda v: v[0] < v[1], lambda v: v[0] == v[1]][type_id](values)
    return versions, int(value), i

def part_1(input):
    return parse(input, 0)[0]

def part_2(input):
    return parse(input, 0)[1]

with open("2021/Day16_input.txt") as f:
    input = ''.join(f"{int(c,16):04b}" for c in f.read().strip())

    print(f"Part 1: {part_1(input)}")
    print(f"Part 2: {part_2(input)}")
