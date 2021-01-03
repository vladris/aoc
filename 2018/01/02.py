f, fs = 0, {0}
while True:
    for line in open("input").readlines():
        f += int(line)
        if f in fs:
            print(f)
            exit()
        fs.add(f)
