def solvable(target, values, concat):
    if len(values) == 1:
        return target == values[0]
    *rest, last = values
    if target % last == 0 and solvable(target // last, rest, concat):
        return True
    if target >= last and solvable(target - last, rest, concat):
        return True
    tail = str(last)
    return (concat and len(str(target)) > len(tail) and str(target).endswith(tail)
            and solvable(int(str(target)[:-len(tail)]), rest, concat))

def part_1(equations):
    return sum(target for target,values in equations if solvable(target, values, False))

def part_2(equations):
    return sum(target for target,values in equations if solvable(target, values, True))

with open("2024/Day07_input.txt") as f:
    equations = [(int(line.split(':')[0]), [int(v) for v in line.split(':')[1].split()])
                 for line in f.read().splitlines()]

    print(f"Part 1: {part_1(equations)}")
    print(f"Part 2: {part_2(equations)}")
