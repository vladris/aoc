inp = list(open('input').readline())
size = 25 * 6
layers = [inp[i:i + size] for i in range(0, len(inp), size)]

def count(layer, digit):
    return sum([1 for i in layer if i == digit])

l, best = 0, 10 ** 6
for layer in layers:
    zeroes = count(layer, '0')
    if zeroes < best:
        best, l = zeroes, layer

print(count(l, '1') * count(l, '2'))
