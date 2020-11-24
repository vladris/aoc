def cost(x):
    fuel = x // 3 - 2
    return 0 if fuel <= 0 else fuel + cost(fuel)

print(sum([cost(int(x.strip())) for x in open('input')]))