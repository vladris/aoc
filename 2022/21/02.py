tree = {}
for line in open('input').readlines():
    key, value = line.strip().split(': ')
    value = value.split(' ')
    if len(value) == 1:
        value = int(value[0])
    tree[key] = value


def get(key):
    if tree[key] == None or isinstance(tree[key], int):
        return tree[key]
    
    v1, v2 = get(tree[key][0]), get(tree[key][2])

    if v1 == None or v2 == None:
        return None

    match tree[key][1]:
        case '+': return v1 + v2
        case '-': return v1 - v2
        case '*': return v1 * v2
        case '/': return v1 // v2


def solve(key, eq):
    if tree[key] == None:
        return eq

    k1, k2 = tree[key][0], tree[key][2]
    v1, v2 = get(k1), get(k2)

    if v1 == None:
        match tree[key][1]:
            case '+': return solve(k1, eq - v2)
            case '-': return solve(k1, eq + v2)
            case '*': return solve(k1, eq // v2)
            case '/': return solve(k1, eq * v2)
    if v2 == None:
        match tree[key][1]:
            case '+': return solve(k2, eq - v1)
            case '-': return solve(k2, v1 - eq)
            case '*': return solve(k2, eq // v1)
            case '/': return solve(k2, v1 // eq)


tree['humn'] = None
tree['root'][1] = '-'

print(solve('root', 0))
