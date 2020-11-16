def captcha(digits, step):
    return sum(d for i,d in enumerate(digits) if d == digits[(i+step) % len(digits)])

def part_1(input):
    return captcha(input, 1)

def part_2(input):
    return captcha(input, len(input) // 2)

with open("2017/Day01_input.txt") as f:
    input = [int(c) for c in f.read().strip()]

    print(f"Part 1: {part_1(input)}")
    print(f"Part 2: {part_2(input)}")
