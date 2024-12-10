def part_1(lengths):
    disk = [i//2 if i % 2 == 0 else None for i,n in enumerate(lengths) for _ in range(n)]
    i, j = 0, len(disk)-1
    while i < j:
        if disk[i] is not None:
            i += 1
        elif disk[j] is None:
            j -= 1
        else:
            disk[i], disk[j] = disk[j], None
    return sum(i*v for i,v in enumerate(disk) if v is not None)

def part_2(lengths):
    files, frees, pos = [], [], 0
    for i,n in enumerate(lengths):
        (files if i % 2 == 0 else frees).append((pos, n))
        pos += n
    total = 0
    for file_id in reversed(range(len(files))):
        start, size = files[file_id]
        for k,(free_start, free_size) in enumerate(frees):
            if free_start >= start:
                break
            if free_size >= size:
                start = free_start
                frees[k] = (free_start + size, free_size - size)
                break
        total += file_id * sum(range(start, start+size))
    return total

with open("2024/Day09_input.txt") as f:
    lengths = [int(c) for c in f.read().strip()]

    print(f"Part 1: {part_1(lengths)}")
    print(f"Part 2: {part_2(lengths)}")
