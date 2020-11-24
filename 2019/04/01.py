def meets_criteria(pwd):
    min = 0
    for c in pwd:
        if int(c) < min: return False
        min = int(c)
    return len(set(pwd)) < len(pwd)

print(len(list(filter(meets_criteria, map(str, range(272091, 815432))))))