inp = open("input").readlines()
ops, nums = inp[-1].split(), [line.split() for line in inp[:-1]]

total = [0 if op == "+" else 1 for op in ops]
for line in nums:
    for i in range(len(total)):
        if ops[i] == "+":
            total[i] += int(line[i])
        else:
            total[i] *= int(line[i])

print(sum(total))
