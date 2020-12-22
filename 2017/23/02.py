# The input code counts primes between b and c with a step of 17

b = 106700
c = 123700
h = 0

while b <= c:
    for i in range(2, b // 2):
        if b % i == 0:
            h += 1
            break
    b += 17

print(h)