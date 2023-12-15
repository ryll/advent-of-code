def hash(step):
    value = 0
    for c in step:
        value = (value + ord(c)) * 17 % 256
    return value

def part_1(input):
    return sum(hash(step) for step in input)

def part_2(input):
    boxes = [{} for _ in range(256)]
    for step in input:
        if step.endswith('-'):
            boxes[hash(step[:-1])].pop(step[:-1], None)
        else:
            label, focal = step.split('=')
            boxes[hash(label)][label] = int(focal)
    return sum(box * slot * focal for box,lenses in enumerate(boxes, 1)
               for slot,focal in enumerate(lenses.values(), 1))

with open("2023/Day15_input.txt") as f:
    input = f.read().strip().split(',')

    print(f"Part 1: {part_1(input)}")
    print(f"Part 2: {part_2(input)}")
