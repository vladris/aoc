total = 0

for line in open('input').readlines():
    line = list(filter(str.isdigit, line))
    total += int(line[0] + line[-1])

print(total)
