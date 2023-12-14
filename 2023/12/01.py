lines = [line.strip().split(' ') for line in open('input').readlines()]
lines = [(line[0], list(map(int, line[1].split(',')))) for line in lines]

def arrangements(head, tail, broken):
    if not tail:
        springs = [len(run) for run in head.split('.') if run]
        return 1 if springs == broken else 0

    if tail[0] == '?':
        return arrangements(head + '.', tail[1:], broken) + \
            arrangements(head + '#', tail[1:], broken)
    else:
        return arrangements(head + tail[0], tail[1:], broken)

print(sum([arrangements('', line[0], line[1]) for line in lines]))
