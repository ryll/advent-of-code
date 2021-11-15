def part_1(input):
    return sum(sum(c in 'aeiou' for c in s) >= 3
               and any(a == b for a,b in zip(s, s[1:]))
               and not any(bad in s for bad in ('ab','cd','pq','xy'))
               for s in input)

def part_2(input):
    return sum(any(s[i:i+2] in s[i+2:] for i in range(len(s)-1))
               and any(a == b for a,b in zip(s, s[2:]))
               for s in input)

with open("2015/Day05_input.txt") as f:
    input = f.read().split()

    print(f"Part 1: {part_1(input)}")
    print(f"Part 2: {part_2(input)}")
