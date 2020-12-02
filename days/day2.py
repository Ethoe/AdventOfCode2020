def p1(passwordlist):
    total = 0
    for password in passwordlist:
        para = password[0].split("-")
        low = int(para[0])
        high = int(para[1])
        key = password[1][0]
        if low <= password[2].count(key) <= high:
            total += 1
    return total


def p2(passwordlist):
    total = 0
    for password in passwordlist:
        para = password[0].split("-")
        low = int(para[0]) - 1
        high = int(para[1]) - 1
        key = password[1][0]
        if bool(password[2][low] == key) ^ bool(password[2][high] == key):
            total += 1
    return total


with open('../inputs/day2in.txt') as passlist:
    passwords = [x.split() for x in passlist.readlines()]

print(p1(passwords))
print(p2(passwords))
