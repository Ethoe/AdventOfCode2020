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

    def has_fields(self):
        return bool(self.byr and self.iyr and self.eyr and self.hgt and self.hcl and self.ecl and self.pid)

    def is_valid(self):
        res = 1920 <= int(self.byr) <= 2002
        res = res and 2010 <= int(self.iyr) <= 2020
        res = res and 2020 <= int(self.eyr) <= 2030
        res = res and (((self.hgt[-2:] == 'cm' and 150 <= int(self.hgt[:-2]) <= 193) or (self.hgt[-2:] == 'in' and 59 <= int(self.hgt[:-2]) <= 76)) if self.hgt else False)
        res = res and (len(self.hcl) == 7 and self.hcl[0] == "#" and self.hcl[1:].isalnum() if self.hcl else False)
        res = res and (self.ecl == 'amb' or self.ecl == 'blu' or self.ecl == 'brn' or self.ecl == 'gry' or self.ecl == 'grn' or self.ecl == 'hzl' or self.ecl == 'oth')
        res = res and (len(self.pid) == 9 and self.pid.isnumeric() if self.pid else False)
        return res


def both_parts(passports):
    p1total = p2total = 0
    current_pass = Document
    current_pass = Document()
    for line in passports:
        if line == '':
            p1total += int(current_pass.has_fields())
            p2total += int(current_pass.is_valid())
            current_pass = Document()

        items = [item.split(':') for item in line.split()]
        for i in range(len(items)):
            setattr(current_pass, items[i][0], items[i][1])
    p1total += int(current_pass.has_fields())
    p2total += int(current_pass.is_valid())
    print(p1total)
    print(p2total)


with open('../inputs/day4in.txt') as passport_in:
    passport_list = [x.strip() for x in passport_in.readlines()]

both_parts(passport_list)
