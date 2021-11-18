import re

def increment(password):
    chars = list(password)
    i = len(chars) - 1
    while chars[i] == 'z':
        chars[i] = 'a'
        i -= 1
    chars[i] = chr(ord(chars[i]) + 1)
    return ''.join(chars)

def valid(password):
    return (any(ord(a) + 1 == ord(b) and ord(b) + 1 == ord(c) for a,b,c in zip(password, password[1:], password[2:]))
            and not set(password) & set('iol')
            and len(set(re.findall(r'(.)\1', password))) >= 2)

def next_password(password):
    while True:
        password = increment(password)
        if valid(password):
            return password

def part_1(input):
    return next_password(input)

def part_2(input):
    return next_password(next_password(input))

with open("2015/Day11_input.txt") as f:
    input = f.read().strip()

    print(f"Part 1: {part_1(input)}")
    print(f"Part 2: {part_2(input)}")
