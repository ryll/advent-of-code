def part_1(locks, keys):
    return sum(all(a+b <= 5 for a,b in zip(lock, key)) for lock in locks for key in keys)

def part_2(locks, keys):
    return "Merry Christmas!"

with open("2024/Day25_input.txt") as f:
    locks, keys = [], []
    for block in f.read().split("\n\n"):
        rows = block.split()
        heights = [sum(row[j] == '#' for row in rows) - 1 for j in range(len(rows[0]))]
        (locks if rows[0][0] == '#' else keys).append(heights)

    print(f"Part 1: {part_1(locks, keys)}")
    print(f"Part 2: {part_2(locks, keys)}")
