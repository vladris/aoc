import re

lines = open("input").readlines()

total = 0
for line in lines:
    total += len(line) - len(re.sub(r"\\\\|\\\"|\\x..", ".", line)) + 2

print(total)