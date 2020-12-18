from hashlib import md5

def triplet(s):
    for i in range(len(s) - 2):
        if s[i] == s[i + 1] == s[i + 2]:
            return s[i]

def hash(i):
    salt = "qzyelonm"
    return md5((salt + str(i)).encode("utf-8")).hexdigest()

i, n = 0, 0

while n < 64:
    c = triplet(hash(i))
    if c:
        for k in range(i + 1, i + 1001):
            if c * 5 in hash(k):
                n += 1
                break

    i += 1

print(i - 1)
