from heapq import heappush, heappop

SPELLS = [('missile', 53), ('drain', 73), ('shield', 113), ('poison', 173), ('recharge', 229)]

def tick(boss_hp, mana, shield, poison, recharge):
    armor = 7 if shield else 0
    return (boss_hp - 3 * bool(poison), mana + 101 * bool(recharge), armor,
            max(0, shield - 1), max(0, poison - 1), max(0, recharge - 1))

def solve(input, hard=False):
    boss_hp, boss_damage = input
    queue = [(0, 50, 500, boss_hp, 0, 0, 0)]
    seen = set()
    while queue:
        spent, hp, mana, boss, shield, poison, recharge = heappop(queue)
        state = (hp, mana, boss, shield, poison, recharge)
        if state in seen:
            continue
        seen.add(state)

        if hard:
            hp -= 1
            if hp <= 0:
                continue
        boss, mana, _, shield, poison, recharge = tick(boss, mana, shield, poison, recharge)
        if boss <= 0:
            return spent

        for name, cost in SPELLS:
            if cost > mana or (name == 'shield' and shield) or (name == 'poison' and poison) or (name == 'recharge' and recharge):
                continue
            new_hp, new_mana, new_boss = hp, mana - cost, boss
            new_shield, new_poison, new_recharge = shield, poison, recharge
            if name == 'missile':
                new_boss -= 4
            elif name == 'drain':
                new_boss -= 2
                new_hp += 2
            elif name == 'shield':
                new_shield = 6
            elif name == 'poison':
                new_poison = 6
            else:
                new_recharge = 5
            if new_boss <= 0:
                return spent + cost

            new_boss, new_mana, armor, new_shield, new_poison, new_recharge = tick(
                new_boss, new_mana, new_shield, new_poison, new_recharge)
            if new_boss <= 0:
                return spent + cost
            new_hp -= max(1, boss_damage - armor)
            if new_hp <= 0:
                continue
            heappush(queue, (spent + cost, new_hp, new_mana, new_boss, new_shield, new_poison, new_recharge))

def part_1(input):
    return solve(input)

def part_2(input):
    return solve(input, hard=True)

with open("2015/Day22_input.txt") as f:
    input = tuple(int(line.split(': ')[1]) for line in f.read().splitlines())

    print(f"Part 1: {part_1(input)}")
    print(f"Part 2: {part_2(input)}")
