from collections import defaultdict
from itertools import product


def p1(actives, life):
    for _ in range(life):
        next_actives = set()
        next_inactives = defaultdict(int)
        for active in actives:
            count = 0
            for neighbor in product([-1, 0, 1], repeat=len(active)):
                new_coord = tuple([a + b for a, b in zip(active, neighbor)])
                if new_coord in actives and new_coord != active:
                    count += 1
                else:
                    next_inactives[new_coord] += 1
            if 2 <= count <= 3:
                next_actives.add(active)

        for coord, count in next_inactives.items():
            if count == 3:
                next_actives.add(coord)

        actives = next_actives
    return len(actives)


data = [x.strip() for x in open('../inputs/day17in.txt').readlines()]

init_actives = {(x, y, 0) for x, row in enumerate(data)
                for y, character in enumerate(row) if character == '#'}

init_hyperactives = {(x, y, 0, 0) for x, row in enumerate(data)
                     for y, character in enumerate(row) if character == '#'}

print(f'P1: {p1(init_actives, 6)} || P2: {p1(init_hyperactives, 6)}')
