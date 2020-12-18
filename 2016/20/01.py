input = open("input").readlines()

blocked = [tuple(map(int, line.split("-"))) for line in input]

i = 0
while True:
    found = True
    for b in blocked:
        if b[0] <= i <= b[1]:
            i, found = b[1], False
            break
    if found:
        break
    i += 1
    
print(i)
