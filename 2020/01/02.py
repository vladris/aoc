numbers = set(map(int, open("input").readlines()))

for n in numbers:
    total = 2020 - n
    s = numbers - { n }

    for n2 in s:
        if total - n2 in s:
            print(n * n2 * (total -n2))
            exit()
