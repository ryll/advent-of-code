def enhance(algorithm, image, steps):
    background = '.'
    for _ in range(steps):
        rows, cols = range(-1, len(image)+1), range(-1, len(image[0])+1)
        get = lambda i,j: image[i][j] if 0 <= i < len(image) and 0 <= j < len(image[0]) else background
        image = [''.join(algorithm[int(''.join('1' if get(i+di, j+dj) == '#' else '0'
                                               for di in (-1,0,1) for dj in (-1,0,1)), 2)]
                         for j in cols) for i in rows]
        background = algorithm[0 if background == '.' else 511]
    return sum(row.count('#') for row in image)

def part_1(algorithm, image):
    return enhance(algorithm, image, 2)

def part_2(algorithm, image):
    return enhance(algorithm, image, 50)

with open("2021/Day20_input.txt") as f:
    algorithm, image = f.read().split("\n\n")
    algorithm = algorithm.replace('\n', '')
    image = image.split()

    print(f"Part 1: {part_1(algorithm, image)}")
    print(f"Part 2: {part_2(algorithm, image)}")
