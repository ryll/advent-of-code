def summed(serial):
    table = [[0] * 301 for _ in range(301)]
    for y in range(1, 301):
        for x in range(1, 301):
            power = ((x + 10) * y + serial) * (x + 10) // 100 % 10 - 5
            table[y][x] = power + table[y-1][x] + table[y][x-1] - table[y-1][x-1]
    return table

def best(table, sizes):
    return max((table[y+s][x+s] - table[y][x+s] - table[y+s][x] + table[y][x], x+1, y+1, s)
               for s in sizes for y in range(301-s) for x in range(301-s))

def part_1(input):
    _, x, y, _ = best(summed(input), [3])
    return f"{x},{y}"

def part_2(input):
    _, x, y, s = best(summed(input), range(1, 301))
    return f"{x},{y},{s}"

with open("2018/Day11_input.txt") as f:
    input = int(f.read().strip())

    print(f"Part 1: {part_1(input)}")
    print(f"Part 2: {part_2(input)}")
