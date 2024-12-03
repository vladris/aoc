import re

inp = open("input").read()

regex = re.compile("mul\((\d+),(\d+)\)", re.MULTILINE)

print(sum([int(match[1]) * int(match[2]) for match in regex.finditer(inp)]))
