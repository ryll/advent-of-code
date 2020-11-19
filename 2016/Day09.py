def length(data, recursive):
    total, i = 0, 0
    while i < len(data):
        if data[i] != '(':
            total += 1
            i += 1
            continue
        close = data.index(')', i)
        size, times = (int(v) for v in data[i+1:close].split('x'))
        chunk = data[close+1:close+1+size]
        total += times * (length(chunk, recursive) if recursive else size)
        i = close + 1 + size
    return total

def part_1(data):
    return length(data, False)

def part_2(data):
    return length(data, True)

with open("2016/Day09_input.txt") as f:
    data = f.read().strip()

    print(f"Part 1: {part_1(data)}")
    print(f"Part 2: {part_2(data)}")
