import time


def p1(sequence, end):
    round_num = 1
    last_num = sequence[0][-1]
    mem = {}
    for item in sequence[0]:
        mem[int(item)] = round_num
        round_num += 1
    while True:
        if last_num in mem:
            spoken = round_num - 1 - mem[last_num]
            mem[last_num] = round_num - 1
            last_num = spoken
        else:
            mem[last_num] = round_num - 1
            last_num = 0
        if round_num == end:
            return last_num
        round_num += 1


with open('../inputs/day15in.txt') as read:
    init_numbers = [x.strip().split(',') for x in read.readlines()]

start = time.time()
p1_v = p1(init_numbers, 2020)
p1_t = time.time() - start
start = time.time()
p2_v = p1(init_numbers, 30000000)
p2_t = time.time() - start

print(f'P1: {p1_v} || P2: {p2_v}')
print(f'P1 Time: {p1_t} || P2 Time: {p2_t}')
