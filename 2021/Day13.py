def fold(dots, axis, value):
    return {(2*value-x if axis == 'x' and x > value else x,
             2*value-y if axis == 'y' and y > value else y) for x,y in dots}

def part_1(dots, folds):
    return len(fold(dots, *folds[0]))

def part_2(dots, folds):
    for axis,value in folds:
        dots = fold(dots, axis, value)
    return '\n' + '\n'.join(''.join('#' if (x,y) in dots else ' ' for x in range(max(dots)[0]+1))
                            for y in range(max(y for _,y in dots)+1))

with open("2021/Day13_input.txt") as f:
    dot_block, fold_block = f.read().split("\n\n")
    dots = {tuple(int(v) for v in line.split(',')) for line in dot_block.split()}
    folds = [(line[11], int(line[13:])) for line in fold_block.splitlines()]

    print(f"Part 1: {part_1(dots, folds)}")
    print(f"Part 2: {part_2(dots, folds)}")
