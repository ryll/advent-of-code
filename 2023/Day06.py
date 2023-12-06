from math import isqrt, prod

def ways(time, distance):
    root = isqrt(time*time - 4*distance)
    lo, hi = (time - root)//2, (time + root)//2
    while lo*(time-lo) <= distance:
        lo += 1
    while hi*(time-hi) <= distance:
        hi -= 1
    return hi - lo + 1

def part_1(times, distances):
    return prod(ways(t, d) for t,d in zip(times, distances))

def part_2(times, distances):
    return ways(int(''.join(map(str, times))), int(''.join(map(str, distances))))

with open("2023/Day06_input.txt") as f:
    times, distances = [[int(v) for v in line.split(': ')[1].split()]
                        for line in f.read().splitlines()]

    print(f"Part 1: {part_1(times, distances)}")
    print(f"Part 2: {part_2(times, distances)}")
