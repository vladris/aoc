from functools import reduce

passports = open("input").read().strip().split('\n\n')

valid = 0
for passport in passports:
    fields = list(map(lambda fld: (fld[:3], fld[4:]), passport.replace('\n', ' ').split(' ')))

    validation = {
        "byr": lambda byr: 1920 <= int(byr) and int(byr) <= 2002,
        "iyr": lambda iyr: 2010 <= int(iyr) and int(iyr) <= 2020,
        "eyr": lambda eyr: 2020 <= int(eyr) and int(eyr) <= 2030,
        "hgt": lambda hgt: 150 <= int(hgt[:-2]) <= 193 if hgt[-2:] == "cm" else
            59 <= int(hgt[:-2]) <= 76 if hgt[-2:] == "in" else False,
        "hcl": lambda hcl: hcl[0] == '#' and int(hcl[1:], 16) != -1,
        "ecl": lambda ecl: ecl in { "amb", "blu", "brn", "gry", "grn", "hzl", "oth" },
        "pid": lambda pid: len(pid) == 9 and int(pid) != -1,
        "cid": lambda cid: False # Ignore
    }

    try:
        if sum(map(lambda fld: validation[fld[0]](fld[1]), fields)) == 7:
            valid += 1
    except:
        pass

print(valid)