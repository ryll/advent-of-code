import re
from functools import cache
from hashlib import md5

def index(salt, stretch):
    @cache
    def digest(i):
        h = md5(f"{salt}{i}".encode()).hexdigest()
        for _ in range(stretch):
            h = md5(h.encode()).hexdigest()
        return h
    found, i = 0, 0
    while True:
        triple = re.search(r'(.)\1\1', digest(i))
        if triple and any(triple[1]*5 in digest(j) for j in range(i+1, i+1001)):
            found += 1
            if found == 64:
                return i
        i += 1

def part_1(salt):
    return index(salt, 0)

def part_2(salt):
    return index(salt, 2016)

with open("2016/Day14_input.txt") as f:
    salt = f.read().strip()

    print(f"Part 1: {part_1(salt)}")
    print(f"Part 2: {part_2(salt)}")
