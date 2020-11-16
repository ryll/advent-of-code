def dance(order, moves):
    programs = list(order)
    for move in moves:
        if move[0] == 's':
            n = int(move[1:]) % len(programs)
            programs = programs[len(programs)-n:] + programs[:len(programs)-n]
        else:
            a, b = move[1:].split('/')
            if move[0] == 'p':
                a, b = programs.index(a), programs.index(b)
            a, b = int(a), int(b)
            programs[a], programs[b] = programs[b], programs[a]
    return ''.join(programs)

def part_1(input):
    return dance('abcdefghijklmnop', input)

def part_2(input):
    seen, order = [], 'abcdefghijklmnop'
    while order not in seen:
        seen.append(order)
        order = dance(order, input)
    return seen[1000000000 % len(seen)]

with open("2017/Day16_input.txt") as f:
    input = f.read().strip().split(',')

    print(f"Part 1: {part_1(input)}")
    print(f"Part 2: {part_2(input)}")
