adapters = sorted(map(int, open("input").readlines()))

adapters = [0] + adapters + [max(adapters) + 3]
cache = { 0: 1 }

def arrangements(i):
    if i in cache:
        return cache[i]

    cache[i] = sum([arrangements(i - j) for j in [1, 2, 3]
        if i - j >= 0 and adapters[i] - adapters[i - j] <= 3])
    return cache[i]

print(arrangements(len(adapters) - 1))
