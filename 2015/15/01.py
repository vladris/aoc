import re

input = open("input").readlines()

ingredients = {}

for line in input:
    m = re.match(r"(\w+):.* (-?\d+).* (-?\d+).* (-?\d+).* (-?\d+).* (\d+)", line)
    ingredients[m[1]] = (int(m[2]), int(m[3]), int(m[4]), int(m[5]))

def score(cnt):
    score = 1
    for i in range(4):
        total = sum(map(lambda x: ingredients[x[0]][i] * x[1], cnt))
        if total <= 0:
            return 0
        score *= total
    return score

best = 0
def mix(ings, cnt, rest):
    global best
    if len(ings) == 1:
        cnt += [(ings[0], rest)]
        best = max(best, score(cnt))
        return

    for i in range(rest - len(ings)):
        mix(ings[1:], cnt + [(ings[0], i)], rest - i)

mix(list(ingredients.keys()), [], 100)
print(best)