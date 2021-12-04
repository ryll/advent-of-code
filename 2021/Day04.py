def wins(board, drawn):
    return any(set(line) <= drawn for line in board + [list(c) for c in zip(*board)])

def scores(numbers, boards):
    drawn, left = set(), list(boards)
    for n in numbers:
        drawn.add(n)
        for board in [b for b in left if wins(b, drawn)]:
            left.remove(board)
            yield n * sum(v for row in board for v in row if v not in drawn)

def part_1(numbers, boards):
    return next(scores(numbers, boards))

def part_2(numbers, boards):
    return list(scores(numbers, boards))[-1]

with open("2021/Day04_input.txt") as f:
    blocks = f.read().split("\n\n")
    numbers = [int(x) for x in blocks[0].split(',')]
    boards = [[[int(x) for x in row.split()] for row in b.splitlines() if row.strip()] for b in blocks[1:]]

    print(f"Part 1: {part_1(numbers, boards)}")
    print(f"Part 2: {part_2(numbers, boards)}")
