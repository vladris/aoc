import re

input = open("input").readlines()

rules, outputs, values = {}, {}, {}

class BotSetter:
    def __init__(self, bot):
        self.bot = bot
        if bot not in values:
            values[bot] = []

    def set(self, value):
        values[self.bot].append(value)

class OutputSetter:
    def __init__(self, out):
        self.out = out

    def set(self, value):
        outputs[self.out] = value

for line in input:
    m = re.match(r"bot (\d+) gives low to (\w+) (\d+) and high to (\w+) (\d+)", line)
    if m:
        l, h = int(m[3]), int(m[5])
        rules[int(m[1])] = (
            BotSetter(l) if m[2] == "bot" else OutputSetter(l),
            BotSetter(h) if m[4] == "bot" else OutputSetter(4),
        )
        continue

    m = re.match(r"value (\d+) goes to bot (\d+)", line)
    v, b = int(m[1]), int(m[2])
    if b not in values:
        values[b] = []
    values[b].append(v)

while not (0 in outputs and 1 in outputs and 2 in outputs):
    for b in values:
        if len(values[b]) == 2:
            l, h = min(values[b]), max(values[b])
            values[b] = []
            rules[b][0].set(l)
            rules[b][1].set(h)

print(outputs[0] * outputs[1] * outputs[2])
