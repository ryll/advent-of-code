def travel(input, start):
    pos, d, letters, steps = start, (1, 0), '', 0
    while input.get(pos, ' ') != ' ':
        if input[pos].isalpha():
            letters += input[pos]
        if input.get((pos[0]+d[0], pos[1]+d[1]), ' ') == ' ':
            for turn in ((d[1], d[0]), (-d[1], -d[0])):
                if input.get((pos[0]+turn[0], pos[1]+turn[1]), ' ') != ' ':
                    d = turn
                    break
        pos = (pos[0]+d[0], pos[1]+d[1])
        steps += 1
    return letters, steps

def part_1(input, start):
    return travel(input, start)[0]

def part_2(input, start):
    return travel(input, start)[1]

with open("2017/Day19_input.txt") as f:
    input = {(i,j): c for i,row in enumerate(f.read().splitlines())
             for j,c in enumerate(row)}
    start = next((i,j) for i,j in sorted(input) if i == 0 and input[(i,j)] == '|')

    print(f"Part 1: {part_1(input, start)}")
    print(f"Part 2: {part_2(input, start)}")
