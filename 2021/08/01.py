lines = open("input").readlines()

total = 0
for line in lines:
    total += sum(1 for d in line.split("|")[1].strip().split(" ") if len(d) in (2, 3, 4, 7))

print(total)
