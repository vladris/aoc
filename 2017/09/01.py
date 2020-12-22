input = "{{<ab>},{<ab>},{<ab>},{<ab>}}"
input = open("input").read().strip()

score, esc, gar, stack = 0, False, False, 0
for c in input:
    if esc:
        esc = False
        continue

    if gar:
        if c == "!":
            esc = True
        elif c == ">":
            gar = False
        continue

    if c == "<":
        gar = True
    elif c == "{":
        stack += 1
    elif c == "}":
        score += stack
        stack -= 1

print(score)
