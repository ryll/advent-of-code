def part_1(input):
    steps, order = {s: set(deps) for s,deps in input.items()}, ''
    while steps:
        step = min(s for s,deps in steps.items() if not deps - set(order))
        order += step
        del steps[step]
    return order

def part_2(input):
    steps, done, workers, time = {s: set(deps) for s,deps in input.items()}, set(), {}, 0
    while steps or workers:
        for step in sorted(s for s,deps in steps.items() if not deps - done):
            if len(workers) < 5:
                workers[step] = time + 60 + ord(step) - 64
                del steps[step]
        time = min(workers.values())
        for step in [s for s,t in workers.items() if t == time]:
            done.add(step)
            del workers[step]
    return time

with open("2018/Day07_input.txt") as f:
    input = {}
    for line in f.read().splitlines():
        input.setdefault(line[5], set())
        input.setdefault(line[36], set()).add(line[5])

    print(f"Part 1: {part_1(input)}")
    print(f"Part 2: {part_2(input)}")
