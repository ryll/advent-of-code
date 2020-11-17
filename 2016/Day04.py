from collections import Counter

def real(name, checksum):
    counts = Counter(name.replace('-', ''))
    return ''.join(sorted(counts, key=lambda c: (-counts[c], c))[:5]) == checksum

def decrypt(name, sector):
    return ''.join(' ' if c == '-' else chr((ord(c) - 97 + sector) % 26 + 97) for c in name)

def part_1(rooms):
    return sum(sector for name,sector,checksum in rooms if real(name, checksum))

def part_2(rooms):
    return next(sector for name,sector,checksum in rooms
                if real(name, checksum) and 'northpole' in decrypt(name, sector))

with open("2016/Day04_input.txt") as f:
    rooms = []
    for line in f.read().split():
        name, rest = line.rsplit('-', 1)
        sector, checksum = rest[:-1].split('[')
        rooms.append((name, int(sector), checksum))

    print(f"Part 1: {part_1(rooms)}")
    print(f"Part 2: {part_2(rooms)}")
