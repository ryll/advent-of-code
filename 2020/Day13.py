def part_1(earliest, buses):
    wait, bus = min(((-earliest) % b, b) for _,b in buses)
    return wait * bus

def part_2(earliest, buses):
    time, step = 0, 1
    for offset,bus in buses:
        while (time + offset) % bus:
            time += step
        step *= bus
    return time

with open("2020/Day13_input.txt") as f:
    earliest, schedule = f.read().split()
    earliest = int(earliest)
    buses = [(i, int(b)) for i,b in enumerate(schedule.split(',')) if b != 'x']

    print(f"Part 1: {part_1(earliest, buses)}")
    print(f"Part 2: {part_2(earliest, buses)}")
