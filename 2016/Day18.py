def safe(row, rows):
    total = 0
    for _ in range(rows):
        total += row.count('.')
        row = ''.join('.^'[left != right] for left,right in zip('.' + row, row[1:] + '.'))
    return total

def part_1(row):
    return safe(row, 40)

def part_2(row):
    return safe(row, 400000)

with open("2016/Day18_input.txt") as f:
    row = f.read().strip()

    print(f"Part 1: {part_1(row)}")
    print(f"Part 2: {part_2(row)}")
