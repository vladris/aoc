lines = open("input").readlines()

total = 0
for line in lines:
    total += len(line.replace("\\", "..").replace("\"", "..")) + 2 - len(line)

print(total)