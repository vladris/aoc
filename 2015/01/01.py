floor = 0
for c in open("input").read():
    floor += 1 if c == '(' else -1

print(floor)