numbers = [int(x) for x in open('input').readline().split(',')]
numbers[1], numbers[2] = 12, 2

i = 0
while numbers[i] != 99:
    op = (lambda x, y: x + y) if numbers[i] == 1 else (lambda x, y: x * y)
    numbers[numbers[i + 3]] = op(numbers[numbers[i + 1]], numbers[numbers[i + 2]])
    i += 4

print(numbers[0])