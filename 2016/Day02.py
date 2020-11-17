MOVES = {'U': (-1,0), 'D': (1,0), 'L': (0,-1), 'R': (0,1)}
SQUARE = ('123', '456', '789')
DIAMOND = ('  1  ', ' 234 ', '56789', ' ABC ', '  D  ')

def code(lines, keypad):
    buttons = {(i,j): c for i,row in enumerate(keypad) for j,c in enumerate(row) if c != ' '}
    i, j = next(p for p,c in buttons.items() if c == '5')
    pressed = ''
    for line in lines:
        for move in line:
            di, dj = MOVES[move]
            if (i+di, j+dj) in buttons:
                i, j = i+di, j+dj
        pressed += buttons[i,j]
    return pressed

def part_1(lines):
    return code(lines, SQUARE)

def part_2(lines):
    return code(lines, DIAMOND)

with open("2016/Day02_input.txt") as f:
    lines = f.read().split()

    print(f"Part 1: {part_1(lines)}")
    print(f"Part 2: {part_2(lines)}")
