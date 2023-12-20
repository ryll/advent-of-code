from collections import deque
from math import lcm

def pulses(modules):
    flipflops = {n: False for n,(kind,_) in modules.items() if kind == '%'}
    conjunctions = {n: {s: False for s,(_,outputs) in modules.items() if n in outputs}
                    for n,(kind,_) in modules.items() if kind == '&'}
    press = 0
    while True:
        press += 1
        queue = deque([('button', 'broadcaster', False)])
        while queue:
            source, target, high = queue.popleft()
            yield press, source, target, high
            if target not in modules:
                continue
            kind, outputs = modules[target]
            if kind == '%':
                if high:
                    continue
                flipflops[target] = out = not flipflops[target]
            elif kind == '&':
                conjunctions[target][source] = high
                out = not all(conjunctions[target].values())
            else:
                out = high
            queue += [(target, output, out) for output in outputs]

def part_1(modules):
    counts = [0, 0]
    for press,_,_,high in pulses(modules):
        if press > 1000:
            return counts[0] * counts[1]
        counts[high] += 1

def part_2(modules):
    feed = next(n for n,(_,outputs) in modules.items() if 'rx' in outputs)
    watched = {n for n,(_,outputs) in modules.items() if feed in outputs}
    cycles = {}
    for press,source,_,high in pulses(modules):
        if high and source in watched and source not in cycles:
            cycles[source] = press
            if len(cycles) == len(watched):
                return lcm(*cycles.values())

with open("2023/Day20_input.txt") as f:
    modules = {}
    for line in f.read().splitlines():
        name, outputs = line.split(' -> ')
        kind = name[0] if name[0] in '%&' else 'b'
        modules[name.lstrip('%&')] = (kind, outputs.split(', '))

    print(f"Part 1: {part_1(modules)}")
    print(f"Part 2: {part_2(modules)}")
