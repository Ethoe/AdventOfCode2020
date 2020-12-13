from functools import reduce



def p1(buses):
    time = buses[0]
    find_min = (float('inf'), 0)
    for bus in buses[1]:
        bus = bus[0]
        wait = int(time / bus)
        wait += 0 if wait * bus == time else 1
        wait = (wait * bus) - time
        if wait < find_min[0]:
            find_min = (wait, bus)
    return find_min[0] * find_min[1]


def p2(buses):
    time = 0
    buses = buses[1]
    while not all([(time + idx) % bus == 0 for bus, idx in buses]):
        time += reduce(lambda x, y: x * y, [bus for bus, idx in buses if (time + idx) % bus == 0])
    return time


with open('../inputs/day13in.txt') as read:
    bus_list = [x.strip() for x in read.readlines()]
bus_list[0] = int(bus_list[0])
bus_list[1] = [(int(x), i) for i, x in enumerate(bus_list[1].split(",")) if x != "x"]

print(f'P1: {p1(bus_list)} || P2: {p2(bus_list)}')
