lines = open("input").readlines()

chunks = {"(": ")", "[": "]", "{": "}", "<": ">"}
points = {")": 3, "]": 57, "}": 1197, ">": 25137}

total = 0
for line in lines:
    stack = []
    for c in line:
        if c in chunks.keys():
            stack.append(chunks[c])
        elif c == "\n":
            break
        elif c == stack.pop():
            continue
        else:
            total += points[c]

print(total)
