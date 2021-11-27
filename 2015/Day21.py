from itertools import combinations, product

WEAPONS = [(8,4,0), (10,5,0), (25,6,0), (40,7,0), (74,8,0)]
ARMOR = [(0,0,0), (13,0,1), (31,0,2), (53,0,3), (75,0,4), (102,0,5)]
RINGS = [(25,1,0), (50,2,0), (100,3,0), (20,0,1), (40,0,2), (80,0,3)]

def loadouts():
    for weapon, armor, rings in product(WEAPONS, ARMOR, [c for n in (0,1,2) for c in combinations(RINGS, n)]):
        items = (weapon, armor) + rings
        yield tuple(sum(stat) for stat in zip(*items))

def wins(damage, armor, boss):
    boss_hp, boss_damage, boss_armor = boss
    return -(-boss_hp // max(1, damage - boss_armor)) <= -(-100 // max(1, boss_damage - armor))

def part_1(input):
    return min(cost for cost,damage,armor in loadouts() if wins(damage, armor, input))

def part_2(input):
    return max(cost for cost,damage,armor in loadouts() if not wins(damage, armor, input))

with open("2015/Day21_input.txt") as f:
    input = tuple(int(line.split(': ')[1]) for line in f.read().splitlines())

    print(f"Part 1: {part_1(input)}")
    print(f"Part 2: {part_2(input)}")
