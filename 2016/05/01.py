from hashlib import md5

input = "ojvtpuvg"
i, pwd = 0, ""

while True:
    hash = md5((input + str(i)).encode("utf-8")).hexdigest()
    if hash[:5] == "00000":
        pwd += hash[5]
    if len(pwd) == 8:
        break
    i += 1

print(pwd)