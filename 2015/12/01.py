import re

input = open("input").read()

nums = re.findall(r"(-?\d+)", input)

print(sum(map(int, nums)))