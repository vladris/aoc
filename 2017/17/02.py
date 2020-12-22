step = 344

pos = 0

for i in range(1, 5 * 10 ** 7 + 1):
    pos = (pos + step) % i + 1
    if pos == 1:
        value = i

print(value)
