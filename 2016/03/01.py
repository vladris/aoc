input = open("input").readlines()

valid = 0
for line in input:
    a, b, c = tuple(map(int, line.split()))
    if a + b > c and a + c > b and b + c > a:
        valid += 1

print(valid)
