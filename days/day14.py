def set_bit(value, bit):
    return value | (1 << bit)


def clear_bit(value, bit):
    return value & ~(1 << bit)


def flip_bit(value, bit):
    return value ^ (1 << bit)


def p1(program):
    total = 0
    mask = ''
    mem = {}
    for line in program:
        if line[0] == 'mask':
            mask = line[2]
        else:
            addr = int(line[0][4:-1])
            value = int(line[2])
            for i in range(len(mask)):
                if mask[i] == '1':
                    value = set_bit(value, len(mask) - i - 1)
                elif mask[i] == '0':
                    value = clear_bit(value, len(mask) - i - 1)
            mem[addr] = value
    for key in mem:
        total += mem[key]

    return total


def p2(program):
    total = 0
    mask = ''
    mem = {}
    for line in program:
        if line[0] == 'mask':
            mask = line[2]
        else:
            addrs = [int(line[0][4:-1])]
            value = int(line[2])
            for i in range(len(mask)):
                if mask[i] == '1':
                    addrs[0] = set_bit(addrs[0], len(mask) - i - 1)
            for i in range(len(mask)):
                if mask[i] == 'X':
                    to_add = []
                    for addr in addrs:
                        to_add.append(flip_bit(addr, len(mask) - i - 1))
                    addrs = addrs + to_add
            for addr in addrs:
                mem[addr] = value
    for key in mem:
        total += mem[key]

    return total


with open('../inputs/day14in.txt') as read:
    init_program = [x.strip().split(' ') for x in read.readlines()]

print(f'P1: {p1(init_program)} || P2: {p2(init_program)}')
