def p2(tickets):
    for seat in range(1, len(tickets)):
        if tickets[seat] != tickets[seat - 1] + 1:
            return tickets[seat - 1] + 1


with open('../inputs/day5in.txt') as phone_scan:
    ticket_list = [int(x.translate(x.maketrans("FBLR", "0101")), 2) for x in phone_scan.readlines()]
print(f"P1: {max(ticket_list)} || P2: {p2(sorted(ticket_list))}")
