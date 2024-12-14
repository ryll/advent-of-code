import re

def tokens(machines, offset):
    total = 0
    for ax,ay,bx,by,px,py in machines:
        px, py = px + offset, py + offset
        determinant = ax*by - ay*bx
        a, b = px*by - py*bx, ax*py - ay*px
        if determinant and a % determinant == 0 and b % determinant == 0:
            total += 3*(a // determinant) + b // determinant
    return total

def part_1(machines):
    return tokens(machines, 0)

def part_2(machines):
    return tokens(machines, 10000000000000)

with open("2024/Day13_input.txt") as f:
    values = [int(v) for v in re.findall(r'\d+', f.read())]
    machines = [values[i:i+6] for i in range(0, len(values), 6)]

    print(f"Part 1: {part_1(machines)}")
    print(f"Part 2: {part_2(machines)}")
