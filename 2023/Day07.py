from collections import Counter

def strength(hand, jokers):
    counts = Counter(hand)
    wild = counts.pop('J', 0) if jokers else 0
    shape = sorted(counts.values(), reverse=True) or [0]
    shape[0] += wild
    order = 'J23456789TQKA' if jokers else '23456789TJQKA'
    return shape, [order.index(c) for c in hand]

def winnings(input, jokers):
    ranked = sorted(input, key=lambda hand: strength(hand[0], jokers))
    return sum(rank * bid for rank,(_,bid) in enumerate(ranked, 1))

def part_1(input):
    return winnings(input, False)

def part_2(input):
    return winnings(input, True)

with open("2023/Day07_input.txt") as f:
    input = [(hand, int(bid)) for hand,bid in (line.split() for line in f.read().splitlines())]

    print(f"Part 1: {part_1(input)}")
    print(f"Part 2: {part_2(input)}")
