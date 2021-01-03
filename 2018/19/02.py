# The program sums the divisors of register 5

n = 10551276

def divs(n):
    i = 1
    while i ** 2 < n:
        if n % i == 0:
            yield i
            yield n // i
        i += 1

print(sum(divs(n)))
