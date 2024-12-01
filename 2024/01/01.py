left, right = list(zip(*map(str.split, open("input").read().splitlines())))

left = sorted(map(int, left))
right = sorted(map(int, right))

print(sum(map(lambda t: abs(t[0] - t[1]), zip(left, right))))
