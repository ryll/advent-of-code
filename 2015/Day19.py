import random

def part_1(input, molecule):
    return len({molecule[:i] + b + molecule[i+len(a):]
                for a,b in input
                for i in range(len(molecule)) if molecule.startswith(a, i)})

def part_2(input, molecule):
    input = list(input)
    while True:
        current, steps = molecule, 0
        while current != 'e':
            for a,b in input:
                if b in current:
                    current = current.replace(b, a, 1)
                    steps += 1
                    break
            else:
                break
        if current == 'e':
            return steps
        random.shuffle(input)

with open("2015/Day19_input.txt") as f:
    replacements, molecule = f.read().split('\n\n')
    input = [tuple(line.split(' => ')) for line in replacements.splitlines()]
    molecule = molecule.strip()

    print(f"Part 1: {part_1(input, molecule)}")
    print(f"Part 2: {part_2(input, molecule)}")
