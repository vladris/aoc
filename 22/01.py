shuffles = [line.strip() for line in open('input').readlines()]

def new_stack(stack):
    return stack[::-1]

def cut(stack, n):
    return stack[n:] + stack[:n]

def deal(stack, n):
    result = stack[:]
    for i, v in enumerate(stack):
        result[(i * n) % len(stack)] = v
    return result

deck = list(range(10007))

for shuffle in shuffles:
    if shuffle.startswith('deal with increment'):
        deck = deal(deck, int(shuffle[20:]))
    elif shuffle.startswith('cut'):
        deck = cut(deck, int(shuffle[4:]))
    else:
        deck = new_stack(deck)

print(deck.index(2019))
