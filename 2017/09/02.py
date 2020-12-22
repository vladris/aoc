input = "{{<ab>},{<ab>},{<ab>},{<ab>}}"
input = open("input").read().strip()

score, esc, gar = 0, False, False
for c in input:
    if esc:
        esc = False
        continue

    if gar:
        if c == "!":
            esc = True
        elif c == ">":
            gar = False
        else:
            score += 1
        continue

    if c == "<":
        gar = True

print(score)
