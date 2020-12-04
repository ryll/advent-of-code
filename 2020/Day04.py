import re

FIELDS = {
    'byr': lambda v: 1920 <= int(v) <= 2002,
    'iyr': lambda v: 2010 <= int(v) <= 2020,
    'eyr': lambda v: 2020 <= int(v) <= 2030,
    'hgt': lambda v: re.fullmatch(r"1[5-8]\dcm|19[0-3]cm|59in|6\din|7[0-6]in", v),
    'hcl': lambda v: re.fullmatch(r"#[0-9a-f]{6}", v),
    'ecl': lambda v: v in ('amb','blu','brn','gry','grn','hzl','oth'),
    'pid': lambda v: re.fullmatch(r"\d{9}", v),
}

def part_1(input):
    return sum(FIELDS.keys() <= p.keys() for p in input)

def part_2(input):
    return sum(FIELDS.keys() <= p.keys() and all(f(p[k]) for k,f in FIELDS.items()) for p in input)

with open("2020/Day04_input.txt") as f:
    input = [dict(x.split(':') for x in block.split()) for block in f.read().split("\n\n")]

    print(f"Part 1: {part_1(input)}")
    print(f"Part 2: {part_2(input)}")
