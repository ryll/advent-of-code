def checksum(data, length):
    while len(data) < length:
        data += '0' + ''.join('01'[c == '0'] for c in reversed(data))
    data = data[:length]
    while len(data) % 2 == 0:
        data = ''.join('01'[a == b] for a,b in zip(data[::2], data[1::2]))
    return data

def part_1(data):
    return checksum(data, 272)

def part_2(data):
    return checksum(data, 35651584)

with open("2016/Day16_input.txt") as f:
    data = f.read().strip()

    print(f"Part 1: {part_1(data)}")
    print(f"Part 2: {part_2(data)}")
