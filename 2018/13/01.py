grid = [[c for c in line.strip("\n")] for line in open("input").readlines()]
carts = []

for i in range(len(grid)):
    for j in range(len(grid[0])):
        c = grid[i][j]
        if c not in "<>^v":
            continue

        carts.append([i, j, c, 0])
        if c in "<>":
            grid[i][j] = "-"
        else:
            grid[i][j] = "|"

while True:
    for cart in sorted(carts, key=lambda c: (c[0], c[1])):
        if cart[2] == ">":
            cart[1] += 1
            if grid[cart[0]][cart[1]] == "\\":
                cart[2] = "v"
            elif grid[cart[0]][cart[1]] == "/":
                cart[2] = "^"
            elif grid[cart[0]][cart[1]] == "+":
                if cart[3] == 0:
                    cart[2] = "^"
                elif cart[3] == 2:
                    cart[2] = "v"
                cart[3] = (cart[3] + 1) % 3
        elif cart[2] == "<":
            cart[1] -= 1
            if grid[cart[0]][cart[1]] == "\\":
                cart[2] = "^"
            elif grid[cart[0]][cart[1]] == "/":
                cart[2] = "v"
            elif grid[cart[0]][cart[1]] == "+":
                if cart[3] == 0:
                    cart[2] = "v"
                elif cart[3] == 2:
                    cart[2] = "^"
                cart[3] = (cart[3] + 1) % 3
        elif cart[2] == "^":
            cart[0] -= 1
            if grid[cart[0]][cart[1]] == "\\":
                cart[2] = "<"
            elif grid[cart[0]][cart[1]] == "/":
                cart[2] = ">"
            elif grid[cart[0]][cart[1]] == "+":
                if cart[3] == 0:
                    cart[2] = "<"
                elif cart[3] == 2:
                    cart[2] = ">"
                cart[3] = (cart[3] + 1) % 3
        elif cart[2] == "v":
            cart[0] += 1
            if grid[cart[0]][cart[1]] == "\\":
                cart[2] = ">"
            elif grid[cart[0]][cart[1]] == "/":
                cart[2] = "<"
            elif grid[cart[0]][cart[1]] == "+":
                if cart[3] == 0:
                    cart[2] = ">"
                elif cart[3] == 2:
                    cart[2] = "<"
                cart[3] = (cart[3] + 1) % 3

        for other in carts:
            if other == cart:
                continue

            if cart[0] == other[0] and cart[1] == other[1]:
                print(f"{cart[1]},{cart[0]}")
                exit()
