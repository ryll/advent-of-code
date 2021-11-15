def part_1(input):
    return sum(2*(l*w + w*h + h*l) + min(l*w, w*h, h*l) for l,w,h in input)

def part_2(input):
    return sum(2*(l + w + h - max(l,w,h)) + l*w*h for l,w,h in input)

with open("2015/Day02_input.txt") as f:
    input = [[int(x) for x in line.split('x')] for line in f.read().split()]

    print(f"Part 1: {part_1(input)}")
    print(f"Part 2: {part_2(input)}")
