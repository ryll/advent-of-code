OPS = {'AND': lambda a,b: a & b, 'OR': lambda a,b: a | b, 'XOR': lambda a,b: a ^ b}

def part_1(wires, gates):
    values = dict(wires)
    def value(wire):
        if wire not in values:
            a, op, b = gates[wire]
            values[wire] = OPS[op](value(a), value(b))
        return values[wire]
    outputs = sorted((w for w in gates if w.startswith('z')), reverse=True)
    return int(''.join(str(value(z)) for z in outputs), 2)

def part_2(wires, gates):
    last = max(w for w in gates if w.startswith('z'))
    feeds = {}
    for a,op,b in gates.values():
        feeds.setdefault(a, set()).add(op)
        feeds.setdefault(b, set()).add(op)
    wrong = set()
    for out,(a,op,b) in gates.items():
        inputs = a[0] in 'xy' and b[0] in 'xy'
        if out.startswith('z') and out != last and op != 'XOR':
            wrong.add(out)
        elif op == 'XOR' and not out.startswith('z') and not inputs:
            wrong.add(out)
        elif op == 'XOR' and inputs and 'x00' not in (a,b) and feeds.get(out, set()) != {'XOR', 'AND'}:
            wrong.add(out)
        elif op == 'AND' and 'x00' not in (a,b) and feeds.get(out, set()) - {'OR'}:
            wrong.add(out)
    return ','.join(sorted(wrong))

with open("2024/Day24_input.txt") as f:
    wire_block, gate_block = f.read().split("\n\n")
    wires = {line.split(': ')[0]: int(line.split(': ')[1]) for line in wire_block.splitlines()}
    gates = {}
    for line in gate_block.splitlines():
        a, op, b, _, out = line.split()
        gates[out] = (a, op, b)

    print(f"Part 1: {part_1(wires, gates)}")
    print(f"Part 2: {part_2(wires, gates)}")
