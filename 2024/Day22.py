from collections import Counter

def evolve(n):
    n = (n ^ (n << 6)) % 16777216
    n = (n ^ (n >> 5)) % 16777216
    return (n ^ (n << 11)) % 16777216

def part_1(seeds):
    total = 0
    for n in seeds:
        for _ in range(2000):
            n = evolve(n)
        total += n
    return total

def part_2(seeds):
    bananas = Counter()
    for n in seeds:
        prices = [n % 10]
        for _ in range(2000):
            n = evolve(n)
            prices.append(n % 10)
        seen = set()
        for i in range(4, len(prices)):
            changes = tuple(prices[j] - prices[j-1] for j in range(i-3, i+1))
            if changes not in seen:
                seen.add(changes)
                bananas[changes] += prices[i]
    return max(bananas.values())

with open("2024/Day22_input.txt") as f:
    seeds = [int(v) for v in f.read().split()]

    print(f"Part 1: {part_1(seeds)}")
    print(f"Part 2: {part_2(seeds)}")
