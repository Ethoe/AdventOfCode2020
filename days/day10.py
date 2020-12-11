def p1(adapters):
    sorted_list = sorted(adapters)
    one_diff = three_diff = prev = 0
    for i in sorted_list:
        if i - prev == 1:
            one_diff += 1
        elif i - prev == 3:
            three_diff += 1
        prev = i
    return one_diff * (three_diff + 1)


def p2(adapters):
    adapters = adapters + [0, max(adapters) + 3]
    sort_a = sorted(adapters)
    counts = [0 for i in range(len(sort_a))]
    counts[0] = 1
    for i in range(1, len(sort_a)):
        curr = sort_a[i]
        for attempt in range(1, 4):
            if i - attempt >= 0 and curr - sort_a[i - attempt] <= 3:
                counts[i] += counts[i - attempt]

    return counts[len(sort_a) - 1]


with open('../inputs/day10in.txt') as read:
    adapter_list = [int(x.strip()) for x in read.readlines()]

print(f'P1: {p1(adapter_list)} || P2: {p2(adapter_list)}')
