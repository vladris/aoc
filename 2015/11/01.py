pwd = "cqjxjnds"

def inc(pwd):
    return pwd[:-1] + chr(ord(pwd[-1]) + 1) if pwd[-1] != "z" else inc(pwd[:-1]) + "a"

def valid(pwd):
    ok = False
    for i in range(len(pwd) - 2):
        if ord(pwd[i]) == ord(pwd[i + 1]) - 1 and ord(pwd[i + 1]) == ord(pwd[i + 2]) - 1:
           ok = True
           break
    
    if not ok: return False

    if sum([c in pwd for c in "iol"]) > 0: return False

    i, ok = 0, 0
    while i < len(pwd) - 1:
        if pwd[i] == pwd[i + 1]:
            ok += 1
            i += 1
        i += 1
    return ok >= 2

while not valid(pwd):
    pwd = inc(pwd)

print(pwd)