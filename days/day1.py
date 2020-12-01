def expense1(expenses):
    check = set()
    for exp in expenses:
        if (2020 - exp) in check:
            return exp * (2020 - exp)
        check.add(exp)


def expense2(expenses):
    check = {}
    for i in expenses:
        for j in expenses:
            if i != j and i + j < 2020:
                check[i + j] = i * j

    for exp in expenses:
        if (2020 - exp) in check.keys():
            return exp * check[2020 - exp]


with open('../inputs/day1in.txt') as report:
    expense = [int(x) for x in report.readlines()]
print(expense1(expense))
print(expense2(expense))
