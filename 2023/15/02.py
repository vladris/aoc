seqs = open('input').read().split(',')

boxes = {i: [] for i in range(256)}

def hash(seq):
    i = 0
    for c in seq:
        i = (i + ord(c)) * 17 % 256
    return i


for seq in seqs:
    #print(boxes)
    if '=' in seq:
        k, v = seq.split('=')
        box = boxes[hash(k)]

        done = False
        for i, lens in enumerate(box):
            if lens[0] == k:
                box[i] = (k, int(v))
                done = True
                break

        if not done:
            box.append((k, int(v)))
    # '-' in seq
    else:
        k = seq[:-1]
        box = boxes[hash(k)]
        for i, lens in enumerate(box):
            if lens[0] == k:
                box.pop(i)
                break

total = 0
for i in boxes:
    for j, lens in enumerate(boxes[i]):
        total += (i + 1) * (j + 1) * lens[1]

print(total)
