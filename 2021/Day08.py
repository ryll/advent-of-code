SIGNATURES = {(6,2,3):0, (2,2,2):1, (5,1,2):2, (5,2,3):3, (4,2,4):4,
              (5,1,3):5, (6,1,3):6, (3,2,2):7, (7,2,4):8, (6,2,4):9}

def decode(patterns, output):
    one = next(p for p in patterns if len(p) == 2)
    four = next(p for p in patterns if len(p) == 4)
    digits = [SIGNATURES[len(d), len(d & one), len(d & four)] for d in output]
    return int(''.join(map(str, digits)))

def part_1(input):
    return sum(len(d) in (2,3,4,7) for _,output in input for d in output)

def part_2(input):
    return sum(decode(patterns, output) for patterns,output in input)

with open("2021/Day08_input.txt") as f:
    input = [[[set(w) for w in part.split()] for part in line.split(' | ')] for line in f.read().splitlines()]

    print(f"Part 1: {part_1(input)}")
    print(f"Part 2: {part_2(input)}")
