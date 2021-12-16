with open("input") as f:
    template = f.readline().strip()
    f.readline()
    insertions = {k: v for k, v in [line.strip().split(" -> ") for line in f.readlines()]}

for _ in range(10):
    elems = [insertions[elem[0] + elem[1]] for elem in zip(template, template[1:])]
    template = "".join([elem[0] + elem[1] for elem in zip(template, elems)]) + template[-1]

count = dict()
for letter in template:
    if letter not in count:
        count[letter] = 0
    count[letter] += 1

print(max(count.values()) - min(count.values()))
