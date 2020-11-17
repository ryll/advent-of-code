import re

def split(address):
    chunks = re.split(r'\[(\w*)\]', address)
    return chunks[::2], chunks[1::2]

def abba(chunk):
    return any(a == d and b == c and a != b for a,b,c,d in zip(chunk, chunk[1:], chunk[2:], chunk[3:]))

def part_1(addresses):
    return sum(any(map(abba, outside)) and not any(map(abba, inside))
               for outside,inside in map(split, addresses))

def part_2(addresses):
    total = 0
    for outside,inside in map(split, addresses):
        abas = {chunk[i:i+3] for chunk in outside for i in range(len(chunk)-2)
                if chunk[i] == chunk[i+2] != chunk[i+1]}
        total += any(b+a+b in chunk for a,b,_ in abas for chunk in inside)
    return total

with open("2016/Day07_input.txt") as f:
    addresses = f.read().split()

    print(f"Part 1: {part_1(addresses)}")
    print(f"Part 2: {part_2(addresses)}")
