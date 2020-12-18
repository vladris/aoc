text = open("input").read().strip()

deco, i = 0, 0
while i < len(text):
    if text[i] != "(":
        deco += 1
        i += 1
        continue

    j = i + 1
    while text[j] != ")":
        j += 1

    l, x = map(int, text[i + 1:j].split("x"))
    deco += l * x
    i = j + 1 + l 

print(deco)
