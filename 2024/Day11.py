from collections import Counter

def blink(stones, times):
    stones = Counter(stones)
    for _ in range(times):
        new = Counter()
        for stone,n in stones.items():
            if stone == 0:
                new[1] += n
            elif len(digits := str(stone)) % 2 == 0:
                new[int(digits[:len(digits)//2])] += n
                new[int(digits[len(digits)//2:])] += n
            else:
                new[stone * 2024] += n
        stones = new
    return sum(stones.values())

def part_1(stones):
    return blink(stones, 25)

def part_2(stones):
    return blink(stones, 75)

with open("2024/Day11_input.txt") as f:
    stones = [int(v) for v in f.read().split()]

    print(f"Part 1: {part_1(stones)}")
    print(f"Part 2: {part_2(stones)}")
