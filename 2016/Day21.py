def rotate(password, n):
    n %= len(password)
    return password[n:] + password[:n]

def apply(password, words, undo):
    if words[1] == 'position' and words[0] == 'swap':
        i, j = int(words[2]), int(words[5])
        password[i], password[j] = password[j], password[i]
    elif words[0] == 'swap':
        i, j = password.index(words[2]), password.index(words[5])
        password[i], password[j] = password[j], password[i]
    elif words[1] in ('left', 'right'):
        steps = int(words[2]) * (1 if words[1] == 'left' else -1)
        password = rotate(password, -steps if undo else steps)
    elif words[0] == 'rotate':
        if undo:
            for n in range(len(password)):
                candidate = rotate(password, n)
                if apply(list(candidate), words, False) == password:
                    password = candidate
                    break
        else:
            i = password.index(words[6])
            password = rotate(password, -(1 + i + (i >= 4)))
    elif words[0] == 'reverse':
        i, j = int(words[2]), int(words[4])
        password[i:j+1] = password[i:j+1][::-1]
    elif words[0] == 'move':
        i, j = int(words[2]), int(words[5])
        if undo:
            i, j = j, i
        password.insert(j, password.pop(i))
    return password

def scramble(password, operations, undo):
    password = list(password)
    for line in (reversed(operations) if undo else operations):
        password = apply(password, line.split(), undo)
    return ''.join(password)

def part_1(operations):
    return scramble('abcdefgh', operations, False)

def part_2(operations):
    return scramble('fbgdceah', operations, True)

with open("2016/Day21_input.txt") as f:
    operations = f.read().splitlines()

    print(f"Part 1: {part_1(operations)}")
    print(f"Part 2: {part_2(operations)}")
