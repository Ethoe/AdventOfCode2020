import copy


def p1(boot):
    acc = pointer = 0
    while True:
        if pointer >= len(boot):
            return acc, True
        verb = boot[pointer][0]
        action = int(boot[pointer][1])
        if verb == 'acc':
            acc += action
        elif verb == 'jmp':
            pointer += action - 1
        elif verb == 'rep':
            return acc, False
        boot[pointer][0] = 'rep'
        pointer += 1


def p2(boot):
    res = 0
    tries = 0
    for i in range(len(boot)):
        if boot[i][0] == 'nop':
            tries += 1
            temp = copy.deepcopy(boot)
            temp[i][0] = 'jmp'
            res, test = p1(temp)
            if test:
                return res
        elif boot[i][0] == 'jmp':
            tries += 1
            temp = copy.deepcopy(boot)
            temp[i][0] = 'nop'
            res, test = p1(temp)
            if test:
                return res
    return tries


with open('../inputs/day8in.txt') as i:
    boot_code = [x.strip().split() for x in i.readlines()]
temp = copy.deepcopy(boot_code)

print(f'P1: {p1(temp)[0]} || P2: {p2(boot_code)}')
