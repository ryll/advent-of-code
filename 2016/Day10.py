def run(values, rules):
    bots, outputs, compared = {}, {}, {}
    for bot,value in values:
        bots.setdefault(bot, []).append(value)
    ready = [bot for bot,chips in bots.items() if len(chips) == 2]
    while ready:
        bot = ready.pop()
        low, high = sorted(bots[bot])
        compared[low,high] = bot
        bots[bot] = []
        for (kind,target),chip in zip(rules[bot], (low, high)):
            if kind == 'output':
                outputs[target] = chip
            else:
                bots.setdefault(target, []).append(chip)
                if len(bots[target]) == 2:
                    ready.append(target)
    return compared, outputs

def part_1(values, rules):
    return run(values, rules)[0][17,61]

def part_2(values, rules):
    outputs = run(values, rules)[1]
    return outputs[0] * outputs[1] * outputs[2]

with open("2016/Day10_input.txt") as f:
    values, rules = [], {}
    for line in f.read().splitlines():
        words = line.split()
        if words[0] == 'value':
            values.append((int(words[5]), int(words[1])))
        else:
            rules[int(words[1])] = ((words[5], int(words[6])), (words[10], int(words[11])))

    print(f"Part 1: {part_1(values, rules)}")
    print(f"Part 2: {part_2(values, rules)}")
