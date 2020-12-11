import json
import re

input = open("input").read()

j = json.loads(input)

def total(j):
    if isinstance(j, list):
        return sum(map(total, j))

    if not isinstance(j, dict):
        return j if isinstance(j, int) else 0

    for k in j:
        if j[k] == "red":
            return 0
        j[k] = total(j[k])

    return sum(j.values())

print(total(j))