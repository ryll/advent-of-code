import re
from collections import Counter

def intersect(a, b):
    box = tuple(max(a[i], b[i]) if i % 2 == 0 else min(a[i], b[i]) for i in range(6))
    return box if all(box[i] <= box[i+1] for i in (0,2,4)) else None

def reboot(input):
    counts = Counter()
    for state,box in input:
        for other,sign in list(counts.items()):
            if (overlap := intersect(box, other)):
                counts[overlap] -= sign
        counts[box] += state
    return sum(sign * (b[1]-b[0]+1) * (b[3]-b[2]+1) * (b[5]-b[4]+1) for b,sign in counts.items())

def part_1(input):
    return reboot([(s,b) for s,b in input if all(-50 <= v <= 50 for v in b)])

def part_2(input):
    return reboot(input)

with open("2021/Day22_input.txt") as f:
    input = [(line.startswith('on'), tuple(int(v) for v in re.findall(r"-?\d+", line)))
             for line in f.read().splitlines()]

    print(f"Part 1: {part_1(input)}")
    print(f"Part 2: {part_2(input)}")
