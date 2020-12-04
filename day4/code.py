passport_list = []
valid_passports = 0

with open('input.txt') as f:
    passport_list = f.read().split('\n\n')

def check_valid(s):
    rf = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

    for i in rf:
        if i not in s:
            return False
    return True

for item in passport_list:
    if check_valid(item):
        valid_passports += 1

print(valid_passports)
