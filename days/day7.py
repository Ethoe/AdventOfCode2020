from _collections import defaultdict


def decode(rules):
    res = defaultdict(list)
    for rule in rules:
        rule_color = f'{rule[0]} {rule[1]}'
        numb = 4
        loop = True
        if rule[numb] == 'no':
            res[rule_color] = []
        else:
            while loop:
                in_rule = f'{rule[numb + 1]} {rule[numb + 2]}'
                number = int(rule[numb])
                res[rule_color].append((number, in_rule))
                if rule[numb + 3][-1] == '.':
                    loop = False
                numb += 4

    return res


def target_in_rule(rule_map, target, rule):
    if not rule_map[rule]:
        return False
    res = False
    for bag in rule_map[rule]:
        if bag[1] == target:
            return True
        else:
            res = res or target_in_rule(rule_map, target, bag[1])
    return res


def total_bags(rule_map, target):
    sum = 0
    if not rule_map[target]:
        return 0
    for bag in rule_map[target]:
        sum += bag[0] + bag[0] * total_bags(rule_map, bag[1])
    return sum


def p1(rules, target):
    rule_map = decode(rules)
    total = 0
    for rule in rule_map:
        total += int(target_in_rule(rule_map, target, rule))
    return total


def p2(rules, target):
    rule_map = decode(rules)
    return total_bags(rule_map, target)


with open('../inputs/day7in.txt') as i:
    rules_tokens = [x.strip().split() for x in i.readlines()]

print(f'P1: {p1(rules_tokens, "shiny gold")} || P2: {p2(rules_tokens, "shiny gold")}')
