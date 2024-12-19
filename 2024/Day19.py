from functools import cache

def arrangements(design, towels):
    @cache
    def count(i):
        if i == len(design):
            return 1
        return sum(count(i + len(t)) for t in towels if design.startswith(t, i))
    return count(0)

def part_1(towels, designs):
    return sum(arrangements(d, towels) > 0 for d in designs)

def part_2(towels, designs):
    return sum(arrangements(d, towels) for d in designs)

with open("2024/Day19_input.txt") as f:
    towel_block, design_block = f.read().split("\n\n")
    towels = tuple(towel_block.strip().split(', '))
    designs = design_block.split()

    print(f"Part 1: {part_1(towels, designs)}")
    print(f"Part 2: {part_2(towels, designs)}")
