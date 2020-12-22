input = open("input").readlines()

valid = 0
for line in input:
    words = line.strip().split(" ")
    if len(set(words)) == len(words):
        valid += 1

print(valid)
