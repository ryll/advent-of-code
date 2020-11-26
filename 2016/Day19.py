def part_1(elves):
    return 2 * (elves - 2**(elves.bit_length() - 1)) + 1

def part_2(elves):
    power = 1
    while power * 3 < elves:
        power *= 3
    if elves == power:
        return elves
    return elves - power if elves <= 2*power else 2*elves - 3*power

with open("2016/Day19_input.txt") as f:
    elves = int(f.read())

    print(f"Part 1: {part_1(elves)}")
    print(f"Part 2: {part_2(elves)}")
