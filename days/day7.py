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


def target_in_rule(rules, target, rule):
    if not rules[rule]:
        return False
    res = False
    for bag in rules[rule]:
        if bag[1] == target:
            return True
        else:
            res = res or target_in_rule(rules, target, bag[1])
    return res


def total_bags(rules, target):
    sum = 0
    if not rules[target]:
        return 0
    for bag in rules[target]:
        sum += bag[0] + bag[0] * total_bags(rules, bag[1])
    return sum


def p1(rules, target):
    total = 0
    for rule in rules:
        total += int(target_in_rule(rules, target, rule))
    return total


def p2(rules, target):
    return total_bags(rules, target)


with open('../inputs/day7in.txt') as i:
    rules_tokens = [x.strip().split() for x in i.readlines()]
rule_map = decode(rules_tokens)

print(f'P1: {p1(rule_map, "shiny gold")} || P2: {p2(rule_map, "shiny gold")}')
