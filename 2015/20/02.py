def house(h):
    fact, i = set(), 1
    while i ** 2 <= h:
        if h % i == 0:
            if h // i <= 50:
                fact.add(i)
            if i <= 50:
                fact.add(h // i)
        i += 1

    return sum(fact)

i = 7 * 10 ** 5
while house(i) < 33100000 // 11:
    i += 1

print(i)
