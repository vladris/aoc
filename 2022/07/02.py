root = {}
pwd = root

for line in open('input').readlines():
    if line[0] == '$':
        match line.strip()[5:]:
            case '': pass
            case '/': pwd = root
            case '..': pwd = pwd['..']
            case name: pwd = pwd[name]
    else:
        info, name = line.strip().split(' ')
        pwd[name] = int(info) if info != 'dir' else {'..': pwd}


def size(d):
    return sum([d[k] if type(d[k]) is int else size(d[k])
                for k in d if k != '..'])


def find(d, needed, best=10 ** 10):
    if (s := size(d)) >= needed:
        best = min(s, best)

    for k in d:
        if k == '..':
            continue
        if type(d[k]) is dict:
            best = find(d[k], needed, best)

    return best


print(find(root, 30_000_000 - (70_000_000 - size(root))))
