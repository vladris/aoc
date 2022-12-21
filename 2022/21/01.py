tree = {}
for line in open('input').readlines():
    key, value = line.strip().split(': ')
    value = value.split(' ')
    if len(value) == 1:
        value = int(value[0])
    tree[key] = value


def get(key):
    if isinstance(tree[key], int):
        return tree[key]
    
    v1, v2 = get(tree[key][0]), get(tree[key][2])

    match tree[key][1]:
        case '+': return v1 + v2
        case '-': return v1 - v2
        case '*': return v1 * v2
        case '/': return v1 // v2

print(get('root'))
