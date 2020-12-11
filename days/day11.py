import copy


def sit(seats):
    change_list = []
    checks = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for row in range(len(seats)):
        for seat in range(len(seats[row])):
            if seats[row][seat] == 'L':
                change = True
                for v, h in checks:
                    if len(seats) > row + v >= 0 and len(seats[row]) > seat + h >= 0:
                        if seats[row + v][seat + h] == '#':
                            change = False
                if change:
                    change_list.append((row, seat))
    change_seats(seats, change_list, '#')


def abandon(seats):
    change_list = []
    checks = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for row in range(len(seats)):
        for seat in range(len(seats[row])):
            if seats[row][seat] == '#':
                change = 0
                for v, h in checks:
                    if len(seats) > row + v >= 0 and len(seats[row]) > seat + h >= 0:
                        if seats[row + v][seat + h] == '#':
                            change += 1
                if change >= 4:
                    change_list.append((row, seat))
    change_seats(seats, change_list, 'L')


def abandon_p2(seats):
    change_list = []
    checks = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for row in range(len(seats)):
        for seat in range(len(seats[row])):
            if seats[row][seat] == '#':
                change = 0
                for v, h in checks:
                    tv = v
                    th = h
                    while True:
                        if len(seats) > row + tv >= 0 and len(seats[row]) > seat + th >= 0:
                            if seats[row + tv][seat + th] == '#':
                                change += 1
                                break
                            elif seats[row + tv][seat + th] == 'L':
                                break
                            tv += v
                            th += h
                        else:
                            break
                if change >= 5:
                    change_list.append((row, seat))
    change_seats(seats, change_list, 'L')


def sit_p2(seats):
    change_list = []
    checks = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for row in range(len(seats)):
        for seat in range(len(seats[row])):
            if seats[row][seat] == 'L':
                change = True
                for v, h in checks:
                    tv = v
                    th = h
                    while True:
                        if len(seats) > row + tv >= 0 and len(seats[row]) > seat + th >= 0:
                            if seats[row + tv][seat + th] == '#':
                                change = False
                                break
                            elif seats[row + tv][seat + th] == 'L':
                                break
                            tv += v
                            th += h
                        else:
                            break
                if change:
                    change_list.append((row, seat))
    change_seats(seats, change_list, '#')


def count_seats(seats):
    total = 0
    for row in seats:
        total += row.count('#')
    return total


def change_seats(seats, changes, to_change):
    for x, y in changes:
        seats[x][y] = to_change


def p1(seat_list):
    prev = copy.deepcopy(seat_list)
    curr = seat_list
    seating = True
    while True:
        if seating:
            sit(curr)
            seating = False
        else:
            abandon(curr)
            seating = True
        if count_seats(curr) == count_seats(prev):
            return count_seats(seat_list)
        prev = copy.deepcopy(curr)


def p2(seat_list):
    prev = copy.deepcopy(seat_list)
    curr = seat_list
    seating = True
    while True:
        if seating:
            sit_p2(curr)
            seating = False
        else:
            abandon_p2(curr)
            seating = True
        if count_seats(curr) == count_seats(prev):
            return count_seats(seat_list)
        prev = copy.deepcopy(curr)


with open('../inputs/day11in.txt') as read:
    seat_in = [list(x.strip()) for x in read.readlines()]

print(f'P1: {p1(copy.deepcopy(seat_in))} || P2: {p2(copy.deepcopy(seat_in))}')
