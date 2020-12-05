with open('../inputs/day5in.txt') as phone_scan: ticket_list = sorted([int(x.translate(x.maketrans("FBLR", "0101")), 2) for x in phone_scan.readlines()])
for seat in range(1, len(ticket_list)):
    if ticket_list[seat] != ticket_list[seat - 1] + 1: print(f"P1: {max(ticket_list)} || P2: {ticket_list[seat - 1] + 1}")