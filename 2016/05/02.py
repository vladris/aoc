from hashlib import md5

input = "ojvtpuvg"
i, pwd = 0, {}

while True:
    hash = md5((input + str(i)).encode("utf-8")).hexdigest()
    if hash[:5] == "00000":
        p = int(hash[5], 16)
        if p < 8 and p not in pwd:
            pwd[p] = hash[6]
    if len(pwd) == 8:
        break
    i += 1

for i in range(8):
    print(pwd[i], end="")
