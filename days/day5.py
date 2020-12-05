def decode(ticket):
    ticket = ticket.replace('F', '0')
    ticket = ticket.replace('B', '1')
    ticket = ticket.replace('R', '1')
    ticket = ticket.replace('L', '0')
    return int(ticket[:-3], 2), int(ticket[7:], 2)


def p1(tickets):
    return max([decode(ticket)[0] * 8 + decode(ticket)[1] for ticket in tickets])


def p2(tickets):
    seats = sorted([decode(ticket)[0] * 8 + decode(ticket)[1] for ticket in tickets])
    current = seats[0]
    for seat in range(1, len(seats)):
        if seats[seat] != current + 1:
            return current + 1
        current += 1


with open('../inputs/day5in.txt') as phone_scan:
    ticket_list = [x.strip() for x in phone_scan.readlines()]

print(p1(ticket_list))
print(p2(ticket_list))
