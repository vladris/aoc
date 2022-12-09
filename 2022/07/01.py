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


total = 0


def size(d):
    global total
    s = sum([d[k] if type(d[k]) is int else size(d[k])
             for k in d if k != '..'])

    if s <= 100_000:
        total += s
    return s


size(root)
print(total)
