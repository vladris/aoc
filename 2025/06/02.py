inp = open("input").readlines()

total = 0
for i in range(len(inp[-1])):
    if inp[-1][i] == "+":
        result = 0
        op = lambda x, y: x + y
    elif inp[-1][i] == "*":
        result = 1
        op = lambda x, y: x * y

    n = "".join([inp[j][i] for j in range(len(inp) - 1)])
    if (n := n.strip()) != "":
        result = op(result, int(n))
    else:
        total += result

total += result

print(total)