numbers = set(map(int, open("input").readlines()))

for n in numbers:
    if 2020 - n in numbers:
        print(n * (2020 - n))
        break