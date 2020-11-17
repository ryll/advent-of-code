from hashlib import md5
from itertools import count

def interesting(door):
    for i in count():
        digest = md5(f"{door}{i}".encode()).hexdigest()
        if digest.startswith('00000'):
            yield digest

def part_1(door):
    return ''.join(digest[5] for digest,_ in zip(interesting(door), range(8)))

def part_2(door):
    password = {}
    for digest in interesting(door):
        if digest[5] in '01234567' and digest[5] not in password:
            password[digest[5]] = digest[6]
            if len(password) == 8:
                return ''.join(password[str(i)] for i in range(8))

with open("2016/Day05_input.txt") as f:
    door = f.read().strip()

    print(f"Part 1: {part_1(door)}")
    print(f"Part 2: {part_2(door)}")
