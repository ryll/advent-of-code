import re
from itertools import count

GROUP = re.compile(r'(\d+) units each with (\d+) hit points (?:\((.*)\) )?'
                   r'with an attack that does (\d+) (\w+) damage at initiative (\d+)')

def parse(line, army):
    units, hp, modifiers, attack, kind, initiative = GROUP.match(line).groups()
    weak, immune = set(), set()
    for part in (modifiers or '').split('; '):
        if part.startswith('weak to '):
            weak = set(part[8:].split(', '))
        elif part.startswith('immune to '):
            immune = set(part[10:].split(', '))
    return {'army': army, 'units': int(units), 'hp': int(hp), 'weak': weak, 'immune': immune,
            'damage': int(attack), 'kind': kind, 'initiative': int(initiative)}

def power(group):
    return group['units'] * group['damage']

def damage(attacker, defender):
    if attacker['kind'] in defender['immune']:
        return 0
    return power(attacker) * (2 if attacker['kind'] in defender['weak'] else 1)

def fight(groups):
    groups = [dict(g) for g in groups]
    while len({g['army'] for g in groups if g['units'] > 0}) > 1:
        alive = [i for i,g in enumerate(groups) if g['units'] > 0]
        targets, taken = {}, set()
        for i in sorted(alive, key=lambda i: (-power(groups[i]), -groups[i]['initiative'])):
            options = [j for j in alive if groups[j]['army'] != groups[i]['army']
                       and j not in taken and damage(groups[i], groups[j]) > 0]
            if options:
                targets[i] = j = max(options, key=lambda j: (damage(groups[i], groups[j]),
                                                            power(groups[j]),
                                                            groups[j]['initiative']))
                taken.add(j)
        killed = 0
        for i in sorted(targets, key=lambda i: -groups[i]['initiative']):
            if groups[i]['units'] <= 0:
                continue
            defender = groups[targets[i]]
            dead = min(defender['units'], damage(groups[i], defender) // defender['hp'])
            defender['units'] -= dead
            killed += dead
        if not killed:
            return None
    return groups

def part_1(input):
    return sum(g['units'] for g in fight(input))

def part_2(input):
    for boost in count(1):
        result = fight([dict(g, damage=g['damage'] + boost * (g['army'] == 'immune'))
                        for g in input])
        if result and all(g['army'] == 'immune' for g in result if g['units'] > 0):
            return sum(g['units'] for g in result)

with open("2018/Day24_input.txt") as f:
    immune, infection = f.read().split("\n\n")
    input = ([parse(line, 'immune') for line in immune.splitlines()[1:] if line] +
             [parse(line, 'infection') for line in infection.splitlines()[1:] if line])

    print(f"Part 1: {part_1(input)}")
    print(f"Part 2: {part_2(input)}")
