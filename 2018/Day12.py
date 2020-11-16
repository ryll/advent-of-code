def grow(state, rules, generations):
    offset, seen, gen = 0, {}, 0
    while gen < generations:
        state = '....' + state + '....'
        offset -= 2
        state = ''.join(rules.get(state[i-2:i+3], '.') for i in range(2, len(state)-2))
        trimmed = state.lstrip('.')
        offset += len(state) - len(trimmed)
        state = trimmed.rstrip('.')
        gen += 1
        if state in seen:
            previous_gen, previous_offset = seen[state]
            cycle = gen - previous_gen
            offset += (offset - previous_offset) * ((generations - gen) // cycle)
            gen += cycle * ((generations - gen) // cycle)
            seen = {}
        seen[state] = (gen, offset)
    return sum(i + offset for i,c in enumerate(state) if c == '#')

def part_1(state, rules):
    return grow(state, rules, 20)

def part_2(state, rules):
    return grow(state, rules, 50000000000)

with open("2018/Day12_input.txt") as f:
    initial, rest = f.read().split("\n\n")
    state = initial.split(': ')[1].strip()
    rules = dict(line.split(' => ') for line in rest.splitlines() if line)

    print(f"Part 1: {part_1(state, rules)}")
    print(f"Part 2: {part_2(state, rules)}")
