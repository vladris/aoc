line, i = open('input').read(), 0

while len(set(line[i:i+4])) != 4:
    i += 1

print(i + 4)
