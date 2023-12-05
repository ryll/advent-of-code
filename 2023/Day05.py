def locations(ranges, maps):
    for mapping in maps:
        moved = []
        todo = list(ranges)
        while todo:
            lo, hi = todo.pop()
            for dst,src,length in mapping:
                a, b = max(lo, src), min(hi, src+length)
                if a < b:
                    moved.append((a-src+dst, b-src+dst))
                    if lo < a:
                        todo.append((lo, a))
                    if b < hi:
                        todo.append((b, hi))
                    break
            else:
                moved.append((lo, hi))
        ranges = moved
    return min(lo for lo,_ in ranges)

def part_1(seeds, maps):
    return locations([(s, s+1) for s in seeds], maps)

def part_2(seeds, maps):
    return locations([(s, s+n) for s,n in zip(seeds[::2], seeds[1::2])], maps)

with open("2023/Day05_input.txt") as f:
    seed_block, *map_blocks = f.read().split("\n\n")
    seeds = [int(v) for v in seed_block.split(': ')[1].split()]
    maps = [[[int(v) for v in line.split()] for line in block.splitlines()[1:]]
            for block in map_blocks]

    print(f"Part 1: {part_1(seeds, maps)}")
    print(f"Part 2: {part_2(seeds, maps)}")
