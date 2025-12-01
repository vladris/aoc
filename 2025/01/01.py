i, n = 50, 0
for line in open("input").readlines():
    sign = 1 if line[0] == "R" else -1
    i = (i + sign * int(line[1:])) % 100
    if i == 0:
        n += 1

print(n)