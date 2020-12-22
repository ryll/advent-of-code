def candidates(input):
    options = {}
    for ingredients, allergens in input:
        for allergen in allergens:
            options[allergen] = options.get(allergen, ingredients) & ingredients
    return options

def part_1(input):
    suspect = set().union(*candidates(input).values())
    return sum(len(ingredients - suspect) for ingredients,_ in input)

def part_2(input):
    options, found = candidates(input), {}
    while options:
        allergen = min(options, key=lambda a: len(options[a]))
        found[allergen] = options.pop(allergen).pop()
        for rest in options.values():
            rest.discard(found[allergen])
    return ','.join(found[a] for a in sorted(found))

with open("2020/Day21_input.txt") as f:
    input = []
    for line in f.read().splitlines():
        ingredients, _, allergens = line.rstrip(')').partition(' (contains ')
        input.append((set(ingredients.split()), allergens.split(', ')))

    print(f"Part 1: {part_1(input)}")
    print(f"Part 2: {part_2(input)}")
