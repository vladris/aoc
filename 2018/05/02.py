import string

input = list(open("input").read().strip())

def l(input):
    i = 0
    while i < len(input) - 1:
        if input[i].swapcase() == input[i + 1]:
            input.pop(i)
            input.pop(i)
            i -= 2
        i += 1
    return len(input)

best = 10 ** 6
for c in string.ascii_lowercase:
    best = min(best, l(list(filter(lambda x: x.lower() != c, input))))

print(best)
