floor = 0
for i, c in enumerate(open("input").read()):
    floor += 1 if c == '(' else -1
    if floor == -1:
        print(i + 1)
        break