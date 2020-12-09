def two_sum(target, array):
    test = {}
    for i in range(len(array)):
        if array[i] not in test:
            test[target - array[i]] = i + 1
        else:
            return test[array[i]], i + 1
    return None


def p1(data):
    for tp in range(25, len(data)):
        if not two_sum(data[tp], data[tp - 25:tp]):
            return data[tp]


def p2(data):
    target = p1(data)
    for i in range(len(data)):
        total = target
        count = 0
        while total >= 0:
            if total == 0:
                return min(data[i:i + count]) + max(data[i:i + count])
            total -= data[i + count]
            count += 1


with open('../inputs/day9in.txt') as read:
    XMAS = [int(x.strip()) for x in read.readlines()]

print(f'P1: {p1(XMAS)} || P2:{p2(XMAS)}')
