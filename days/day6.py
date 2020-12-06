def p1(groups):
    current = ''
    total = 0
    for group in groups:
        if group == '':
            total += len(current)
            current = ''
        for letter in group:
            if letter not in current:
                current += letter
    total += len(current)
    return total


def p2(groups):
    current = ''
    first = True
    total = 0
    for group in groups:
        if group == '':
            total += len(current)
            current = ''
            first = True

        elif first:
            current = group
            first = False
        else:
            temp = current
            for letter in current:
                if letter not in group:
                    temp = temp.replace(letter, '')
            current = temp
    total += len(current)
    return total


with open('../inputs/day6in.txt') as customs_form:
    answers = [x.strip() for x in customs_form.readlines()]

print(f'P1: {p1(answers)} || P2: {p2(answers)}')
