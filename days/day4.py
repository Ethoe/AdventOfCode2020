class Document:
    def __init__(self):
        self.byr = False
        self.iyr = False
        self.eyr = False
        self.hgt = False
        self.hcl = False
        self.ecl = False
        self.pid = False
        self.cid = False

    def is_valid(self):
        return self.byr and self.iyr and self.eyr and self.hgt and self.hcl and self.ecl and self.pid


def p1(passports):
    total = 0
    current_pass = Document()
    for line in passports:
        if line == '':
            total += int(current_pass.is_valid())
            current_pass = Document()
        items = [item.split(':') for item in line.split()]
        for i in range(len(items)):
            if items[i][0] == 'byr':
                current_pass.byr = True
            elif items[i][0] == 'iyr':
                current_pass.iyr = True
            elif items[i][0] == 'eyr':
                current_pass.eyr = True
            elif items[i][0] == 'hgt':
                current_pass.hgt = True
            elif items[i][0] == 'hcl':
                current_pass.hcl = True
            elif items[i][0] == 'ecl':
                current_pass.ecl = True
            elif items[i][0] == 'pid':
                current_pass.pid = True
            elif items[i][0] == 'cid':
                current_pass.cid = True
    total += int(current_pass.is_valid())
    return total


def p2(passports):
    total = 0
    current_pass = Document()
    for line in passports:
        if line == '':
            total += int(current_pass.is_valid())
            current_pass = Document()
        items = [item.split(':') for item in line.split()]
        for i in range(len(items)):
            if items[i][0] == 'byr' and 1920 <= int(items[i][1]) <= 2002:
                current_pass.byr = True
            elif items[i][0] == 'iyr' and 2010 <= int(items[i][1]) <= 2020:
                current_pass.iyr = True
            elif items[i][0] == 'eyr' and 2020 <= int(items[i][1]) <= 2030:
                current_pass.eyr = True
            elif items[i][0] == 'hgt':
                if items[i][1][-2:] == 'cm' and 150 <= int(items[i][1][:-2]) <= 193:
                    current_pass.hgt = True
                elif items[i][1][-2:] == 'in' and 59 <= int(items[i][1][:-2]) <= 76:
                    current_pass.hgt = True
            elif items[i][0] == 'hcl' and len(items[i][1]) == 7 and items[i][1][0] == "#" \
                    and items[i][1][1:].isalnum():
                current_pass.hcl = True
            elif items[i][0] == 'ecl':
                c = items[i][1]
                if c == 'amb' or c == 'blu' or c == 'brn' or c == 'gry' or c == 'grn' or c == 'hzl' or c == 'oth':
                    current_pass.ecl = True
            elif items[i][0] == 'pid' and len(items[i][1]) == 9 and items[i][1].isnumeric():
                current_pass.pid = True
            elif items[i][0] == 'cid':
                current_pass.cid = True
    total += int(current_pass.is_valid())
    return total


with open('../inputs/day4in.txt') as passport_in:
    passport_list = [x.strip() for x in passport_in.readlines()]

print(p1(passport_list))
print(p2(passport_list))
