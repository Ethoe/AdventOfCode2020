def p1(map, path):
    movement = 0
    total = 0
    for layer in range(0, len(map), path[1]):
        if map[layer][movement] == "#":
            total += 1
        movement = (movement + path[0]) % len(map[0])
    return total


def p2(map, paths):
    total = 1
    for path in paths:
        total *= p1(map, path)
    return total


with open('../inputs/day3in.txt') as treemap:
    layers = [x.strip() for x in treemap.readlines()]

slopes = ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))

print(p2(layers, slopes))
