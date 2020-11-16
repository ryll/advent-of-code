DIRECTIONS = {'^': (-1,0), 'v': (1,0), '<': (0,-1), '>': (0,1)}

def run(track, carts, first_crash):
    while len(carts) > 1:
        carts.sort()
        dead = set()
        for i,cart in enumerate(carts):
            if i in dead:
                continue
            cart[0] += cart[2]
            cart[1] += cart[3]
            piece = track.get((cart[0], cart[1]), ' ')
            if piece == '/':
                cart[2], cart[3] = -cart[3], -cart[2]
            elif piece == '\\':
                cart[2], cart[3] = cart[3], cart[2]
            elif piece == '+':
                if cart[4] % 3 == 0:
                    cart[2], cart[3] = -cart[3], cart[2]
                elif cart[4] % 3 == 2:
                    cart[2], cart[3] = cart[3], -cart[2]
                cart[4] += 1
            for j,other in enumerate(carts):
                if j != i and j not in dead and other[:2] == cart[:2]:
                    if first_crash:
                        return f"{cart[1]},{cart[0]}"
                    dead |= {i, j}
        carts = [c for i,c in enumerate(carts) if i not in dead]
    return f"{carts[0][1]},{carts[0][0]}"

def part_1(track, carts):
    return run(track, [list(c) for c in carts], True)

def part_2(track, carts):
    return run(track, [list(c) for c in carts], False)

with open("2018/Day13_input.txt") as f:
    track, carts = {}, []
    for y,row in enumerate(f.read().splitlines()):
        for x,piece in enumerate(row):
            if piece in DIRECTIONS:
                carts.append((y, x, *DIRECTIONS[piece], 0))
                piece = '-' if piece in '<>' else '|'
            track[(y,x)] = piece

    print(f"Part 1: {part_1(track, carts)}")
    print(f"Part 2: {part_2(track, carts)}")
