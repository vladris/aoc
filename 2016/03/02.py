input = open("input").readlines()

valid = 0
for i in range(0, len(input), 3):
    for col in range(3):
        a, b, c = int(input[i].split()[col]), int(input[i + 1].split()[col]), int(input[i + 2].split()[col])
        if a + b > c and a + c > b and b + c > a:
            valid += 1

print(valid)
