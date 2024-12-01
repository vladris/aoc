left, right = list(zip(*map(str.split, open("input").read().splitlines())))

left = map(int, left)
right = list(map(int, right))

print(sum(
    map(
        lambda l: l * len(list(filter(lambda r: r == l, right))),
        left)))
