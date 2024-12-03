import re

inp = open("input").read()

regex = re.compile("mul\((\d+),(\d+)\)|do\(\)|don't\(\)", re.MULTILINE)

total, enabled = 0, True
for match in regex.finditer(inp):
    match match.group():
        case "do()":
            enabled = True
        case "don't()":
            enabled = False
        case _:
            if enabled:
                total += int(match[1]) * int(match[2])

print(total)
