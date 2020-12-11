from hashlib import md5

input = "yzbqklnj"

i = 0
while True:
    hash = md5((input + str(i)).encode('utf-8')).hexdigest()
    if hash[:6] == "000000":
        print(i)
        break
    i += 1