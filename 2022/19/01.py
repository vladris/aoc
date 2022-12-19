import re
import math


def run(bots, costs, resources, time):
    if best[time] > resources[3]:
        return

    best[time] = resources[3]

    if time == 0:
        return

    for bot_type in range(4):
        dt = math.ceil((costs[bot_type][0] - resources[0]) / bots[0])
        if bot_type >= 2:
            if bots[bot_type - 1] == 0:
                continue

            dt = max(dt, math.ceil((costs[bot_type][1] -
                                    resources[bot_type - 1]) / bots[bot_type - 1]))

        dt = max(dt, 0) + 1

        if time < dt:
            continue

        new_resources = [resources[i] + bots[i] * dt for i in range(4)]
        new_resources[0] -= costs[bot_type][0]
        if bot_type >= 2:
            new_resources[bot_type - 1] -= costs[bot_type][1]

        bots[bot_type] += 1
        run(bots, costs, new_resources, time - dt)
        bots[bot_type] -= 1


score = 0
for i, line in enumerate(open('input').readlines()):
    m = re.match(
        '.*(\d+) ore.*(\d+) ore.*(\d+) ore and (\d+) clay.*(\d+) ore and (\d+) obsidian', line)
    costs = list(map(int, m.groups()))

    costs = [[costs[0]], [costs[1]], [
        costs[2], costs[3]], [costs[4], costs[5]]]

    best = [0] * 25

    run([1, 0, 0, 0], costs, [0] * 4, 24)

    score += (i + 1) * best[0]

print(score)
