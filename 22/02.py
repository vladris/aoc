shuffles = [line.strip() for line in open('input').readlines()]

def new_stack(a, b, n):
    return -a, n - b - 1

def cut(a, b, n, c):
    return a, b + (n - c)

def deal(a, b, n, d):
    return a * d % n, b * d % n

n, e = 119315717514047, 101741582076661

def shuffle_eq(eq, n, shuffles):
    for shuffle in shuffles:
        if shuffle.startswith('deal with increment'):
            eq = deal(*eq, n, int(shuffle[20:]))
        elif shuffle.startswith('cut'):
            eq = cut(*eq, n, int(shuffle[4:]))
        else:
            eq = new_stack(*eq, n)
    return eq

def mul(x, y, n):
    return x[0] * y[0] % n, (x[0] * y[1] + x[1]) % n

def exp(x, n, e):
    res = (1, 0)
    while e > 0:
        if e % 2:
            res = mul(res, x, n)

        e >>= 1
        x = mul(x, x, n)
    return res

res = exp(shuffle_eq((1, 0), n, shuffles), n, e)

print(f'{res[0]} * x + {res[1]} = 2020')

# solve at https://www.dcode.fr/modular-equation-solver 
