inp = [list(line.strip()) for line in open("input").readlines()]

def get(head, tail):
    if len(head) == 12:
        return int("".join(head))

    best_i = 0
    for i in range(1, len(tail) + len(head) - 11):
        if tail[best_i] < tail[i]:
            best_i = i

    return get(head + [tail[best_i]], tail[best_i + 1 :])


total = sum([get([], jolts) for jolts in inp])
print(total)