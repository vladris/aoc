passports = open("input").read().strip().split('\n\n')

valid = 0
for passport in passports:
    fields = set(map(lambda fld: fld[:3], passport.replace('\n', ' ').split(' ')))

    if not { "byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid" } - fields:
        valid += 1

print(valid)