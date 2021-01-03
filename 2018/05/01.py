input = list(open("input").read().strip())

i = 0
while i < len(input) - 1:
    if input[i].swapcase() == input[i + 1]:
        input.pop(i)
        input.pop(i)
        i -= 2
    i += 1

print(len(input))
