passport_list = []
valid_passports = 0

with open('input.txt') as f:
    passport_list = f.read().split('\n\n')

def check_valid(s):
    rf = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    parts = s.split()

    data = []
    for part in parts:
        p = part.split(':')
        data.append(p)

    for i in rf:
        if i not in s:
            return False

    for field in data:
        if field[0] == 'byr':
            year = int(field[1])
            if year < 1920 or year > 2002:
                return False

        elif field[0] == 'iyr':
            year = int(field[1])
            if year < 2010 or year > 2020:
                return False

        elif field[0] == 'eyr':
            year = int(field[1])
            if year < 2020 or year > 2030:
                return False

        elif field[0] == 'hgt':
            if 'cm' in field[1] or 'in' in field[1]:
                num = int(field[1][:-2])
            else:
                return False

            if 'cm' in field[1]:
                if num < 150 or num > 193:
                    return False
            elif 'in' in field[1]:
                if num < 59 or num > 76:
                    return False
            else:
                return False

        elif field[0] == 'hcl':
            color = field[1]
            if color[0] != '#':
                return False
            elif len(color) != 7:
                return False

            allowed_chars = '1234567890abcdef'
            color = color[1:6]
            for c in color:
                if c not in allowed_chars:
                    return False

        elif field[0] == 'ecl':
            allowed_colors = 'amb blu brn gry grn hzl oth'
            if field[1] not in allowed_colors:
                return False

        elif field[0] == 'pid':
            if len(field[1]) != 9:
                return False

    return True

for item in passport_list:
    if check_valid(item):
        valid_passports += 1

print(valid_passports)
