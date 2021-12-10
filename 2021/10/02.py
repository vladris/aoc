lines = open("input").readlines()

chunks = {"(": ")", "[": "]", "{": "}", "<": ">"}
points = {")": 1, "]": 2, "}": 3, ">": 4}

scores = []
for line in lines:
    stack = []
    for c in line:
        if c in chunks.keys():
            stack.append(chunks[c])
        elif c == "\n":
            score = 0
            while stack:
                score = score * 5 + points[stack.pop()]
            scores.append(score) 
            break
        elif c == stack.pop():
            continue
        else:
            break

print(sorted(scores)[len(scores) // 2])
