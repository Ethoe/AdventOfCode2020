import re


class Rules:
    def __init__(self, rules):
        self.rules = {}
        for rule in rules:
            matches = re.match(r'(.*): (.*) or (.*)', rule)
            self.rules[matches.group(1)] = [[int(x) for x in matches.group(2).split('-')], [int(x) for x in matches.group(3).split('-')]]

    def valid_num(self, num):
        for rule in self.rules:
            ranges = self.rules[rule]
            if ranges[0][0] <= num <= ranges[0][1] or ranges[1][0] <= num <= ranges[1][1]:
                return True
        return False

    def valid_ticket(self, ticket):
        invalids = []
        for field in ticket:
            if not self.valid_num(field):
                invalids.append(field)
        return invalids


def p1(tickets, rules):
    errors = []
    to_remove = []
    for i in range(len(tickets)):
        broken = rules.valid_ticket(tickets[i])
        if broken:
            errors = errors + rules.valid_ticket(tickets[i])
            to_remove.append(i)
    for remove in sorted(to_remove, reverse=True):
        del tickets[remove]

    return sum(errors)


with open('../inputs/day16in.txt') as f:
    pin = [x.strip() for x in f.readlines()]

rule_parse = []
for item in pin:
    if item == '':
        break
    rule_parse.append(item)
rule_list = Rules(rule_parse)
ticket_parse = []
your_ticket = ''
at_tickets = False
for i in range(len(pin)):
    if at_tickets:
        ticket_parse.append([int(x) for x in pin[i].split(',')])
    else:
        if pin[i] == 'your ticket:':
            your_ticket = pin[i + 1]
        if pin[i] == 'nearby tickets:':
            at_tickets = True


print(f'P1: {p1(ticket_parse, rule_list)}')
