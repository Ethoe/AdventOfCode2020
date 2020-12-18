def evaluate_expr(stack):
    res = stack.pop() if stack else 0
    while stack and stack[-1] != ')':
        sign = stack.pop()
        if sign == '+':
            res += int(stack.pop())
        else:
            res *= int(stack.pop())
    return res


def calculate(s):
    stack = []
    n, operand = 0, 0

    for i in range(len(s) - 1, -1, -1):
        ch = s[i]
        if ch.isdigit():
            operand = (10 ** n * int(ch)) + operand
            n += 1
        elif ch != " ":
            if n:
                stack.append(operand)
                n, operand = 0, 0
            if ch == '(':
                res = evaluate_expr(stack)
                stack.pop()
                stack.append(res)
            else:
                stack.append(ch)
    if n:
        stack.append(operand)

    return evaluate_expr(stack)


def p1(data):
    res = 0
    for eq in data:
        res += calculate(eq)
    return res


def p2(data):
    res = 0
    for s in data:
        s += '+0'
        stack, num, preOp = [], 0, "+"
        for i in range(len(s)):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            elif not s[i].isspace():
                if preOp == "+":
                    stack.append(num)
                elif preOp == "*":
                    stack.append(stack.pop() * num)
                preOp, num = s[i], 0
        res += sum(stack)
    return res


data = [x.strip().replace(' ', '') for x in open('../inputs/day18in.txt').readlines()]

print(f'P1: {p1(data)} || P2: {p2(data)}')
