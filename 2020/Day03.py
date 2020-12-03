def count_trees(input, right, down):
    return sum(row[i*right % len(row)] == '#' for i,row in enumerate(input[::down]))

def part_1(input):
    return count_trees(input, 3, 1)

def part_2(input):
    answer = 1
    for right,down in [(1,1),(3,1),(5,1),(7,1),(1,2)]:
        answer *= count_trees(input, right, down)
    return answer

with open("2020/Day03_input.txt") as f:
    input = f.read().split()

    print(f"Part 1: {part_1(input)}")
    print(f"Part 2: {part_2(input)}")
