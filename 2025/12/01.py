parts = open("input").read().split("\n\n")

shapes = ["".join(shape.split("\n")[1:]) for shape in parts[:-1]]
regions = []
for region in parts[-1].split("\n"):
    area, reqs = region.split(":")
    x, y = area.split("x")
    reqs = list(map(int, reqs.strip().split(" ")))
    regions.append((int(x), int(y), reqs))

needs = [sum([c == "#" for c in shape]) for shape in shapes]

can_fit = 0
for x, y, reqs in regions:
    lower_bound = sum([r * n for r, n in zip(reqs, needs)])
    upper_bound = sum(reqs) * 9

    if x * y < lower_bound:
        continue
    elif x * y >= upper_bound:
        can_fit += 1
    else:
        raise Exception("Maybe")

print(can_fit)
