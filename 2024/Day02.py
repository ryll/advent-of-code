def safe(report):
    diffs = [b-a for a,b in zip(report, report[1:])]
    return all(1 <= d <= 3 for d in diffs) or all(-3 <= d <= -1 for d in diffs)

def part_1(reports):
    return sum(safe(r) for r in reports)

def part_2(reports):
    return sum(any(safe(r[:i] + r[i+1:]) for i in range(len(r))) for r in reports)

with open("2024/Day02_input.txt") as f:
    reports = [[int(v) for v in line.split()] for line in f.read().splitlines()]

    print(f"Part 1: {part_1(reports)}")
    print(f"Part 2: {part_2(reports)}")
