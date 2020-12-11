import re

input = open("input").readlines()

deer = {}
run = {}

for line in input:
    m = re.match(r"(\w+) can fly (\d+) km/s for (\d+) seconds, .* (\d+) seconds.", line)
    deer[m[1]] = tuple(map(int, [m[2], m[3], m[4]]))
    run[m[1]] = (0, int(m[3]), 0)

for i in range(2503):
    for d in deer:
        if run[d][1] > 0:
            run[d] = (run[d][0] + deer[d][0], run[d][1] - 1, deer[d][2] - 1)
        elif run[d][2] == 0:
            run[d] = (run[d][0], deer[d][1], 0)
        else:
            run[d] = (run[d][0], 0, run[d][2] - 1)

print(max(map(lambda x: x[0], run.values())))