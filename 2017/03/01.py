input = 312051

n = 1 

while n ** 2 < input:
    n += 2

x, y, t = n // 2, n // 2, n ** 2

x -= t - input
print(abs(x) + abs(y))
