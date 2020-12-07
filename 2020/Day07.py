import re

def holds_gold(input, bag):
    return any(inner == 'shiny gold' or holds_gold(input, inner) for _,inner in input[bag])

def count_inside(input, bag):
    return sum(n + n*count_inside(input, inner) for n,inner in input[bag])

def part_1(input):
    return sum(holds_gold(input, bag) for bag in input)

def part_2(input):
    return count_inside(input, 'shiny gold')

with open("2020/Day07_input.txt") as f:
    input = {}
    for line in f:
        bag, contents = line.strip(".\n").split(" bags contain ")
        input[bag] = [(int(n), b) for n,b in re.findall(r"(\d+) (\w+ \w+) bags?", contents)]

    print(f"Part 1: {part_1(input)}")
    print(f"Part 2: {part_2(input)}")
