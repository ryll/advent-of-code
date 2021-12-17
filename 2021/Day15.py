from heapq import heappush, heappop

def dijkstra(grid, size):
    end, seen, queue = (size-1, size-1), set(), [(0, 0, 0)]
    while queue:
        risk, i, j = heappop(queue)
        if (i,j) == end:
            return risk
        if (i,j) in seen:
            continue
        seen.add((i,j))
        for x,y in ((i-1,j), (i+1,j), (i,j-1), (i,j+1)):
            if 0 <= x < size and 0 <= y < size:
                heappush(queue, (risk + grid(x,y), x, y))

def part_1(input):
    size = len(input)
    return dijkstra(lambda i,j: input[i][j], size)

def part_2(input):
    size = len(input)
    return dijkstra(lambda i,j: (input[i%size][j%size] + i//size + j//size - 1) % 9 + 1, size*5)

with open("2021/Day15_input.txt") as f:
    input = [[int(c) for c in row] for row in f.read().split()]

    print(f"Part 1: {part_1(input)}")
    print(f"Part 2: {part_2(input)}")
