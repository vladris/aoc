adapters = sorted(map(int, open("input").readlines()))

adapters = [0] + adapters + [max(adapters) + 3]
diff = { 1: 0, 3: 0 }

for a, b in zip(adapters, adapters[1:]):
    diff[b - a] += 1

print(diff[1] * diff[3])