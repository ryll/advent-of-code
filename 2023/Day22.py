def settle(bricks):
    heights, supports, supported_by = {}, {}, {}
    for i,(x1,y1,z1,x2,y2,z2) in enumerate(sorted(bricks, key=lambda b: b[2])):
        cells = [(x,y) for x in range(x1, x2+1) for y in range(y1, y2+1)]
        top = max((heights[c][0] for c in cells if c in heights), default=0)
        supports[i] = set()
        supported_by[i] = {heights[c][1] for c in cells
                           if c in heights and heights[c][0] == top}
        for j in supported_by[i]:
            supports[j].add(i)
        heights.update({c: (top + z2-z1+1, i) for c in cells})
    return supports, supported_by

def part_1(bricks):
    supports, supported_by = settle(bricks)
    return sum(all(len(supported_by[j]) > 1 for j in supports[i]) for i in supports)

def part_2(bricks):
    supports, supported_by = settle(bricks)
    total = 0
    for i in supports:
        falling, queue = {i}, [i]
        while queue:
            for j in supports[queue.pop()]:
                if j not in falling and supported_by[j] <= falling:
                    falling.add(j)
                    queue.append(j)
        total += len(falling) - 1
    return total

with open("2023/Day22_input.txt") as f:
    bricks = [[int(v) for v in line.replace('~', ',').split(',')]
              for line in f.read().splitlines()]

    print(f"Part 1: {part_1(bricks)}")
    print(f"Part 2: {part_2(bricks)}")
