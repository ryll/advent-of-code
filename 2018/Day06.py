from collections import Counter

def part_1(input):
    lo_x, hi_x = min(x for x,_ in input), max(x for x,_ in input)
    lo_y, hi_y = min(y for _,y in input), max(y for _,y in input)
    areas, infinite = Counter(), set()
    for x in range(lo_x, hi_x+1):
        for y in range(lo_y, hi_y+1):
            distances = sorted((abs(x-a) + abs(y-b), i) for i,(a,b) in enumerate(input))
            if distances[0][0] < distances[1][0]:
                areas[distances[0][1]] += 1
                if x in (lo_x, hi_x) or y in (lo_y, hi_y):
                    infinite.add(distances[0][1])
    return max(n for i,n in areas.items() if i not in infinite)

def part_2(input):
    return sum(sum(abs(x-a) + abs(y-b) for a,b in input) < 10000
               for x in range(min(x for x,_ in input), max(x for x,_ in input)+1)
               for y in range(min(y for _,y in input), max(y for _,y in input)+1))

with open("2018/Day06_input.txt") as f:
    input = [tuple(int(v) for v in line.split(', ')) for line in f.read().splitlines()]

    print(f"Part 1: {part_1(input)}")
    print(f"Part 2: {part_2(input)}")
