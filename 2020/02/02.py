lines = open('input').readlines()

valid = 0
for line in lines:
    pos, letter, password = line.split()
    pos1, pos2 = map(int, pos.split('-'))
    letter = letter[:-1]

    if (password[pos1 - 1] == letter) != (password[pos2 - 1] == letter):
        valid += 1

print(valid)