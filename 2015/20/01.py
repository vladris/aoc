def house(h):
    fact, i = set(), 1
    while i ** 2 <= h:
        if h % i == 0:
            fact.add(i)
            fact.add(h // i)
        i += 1

    return sum(fact)

i = 7 * 10 ** 5
while house(i) < 3310000:
    i += 1

print(i)
