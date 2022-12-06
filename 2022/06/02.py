line, i = open('input').read(), 0

while len(set(line[i:i+14])) != 14:
    i += 1

print(i + 14)
