from hashlib import md5

input = "yzbqklnj"

i = 0
while True:
    hash = md5((input + str(i)).encode('utf-8')).hexdigest()
    if hash[:5] == "00000":
        print(i)
        break
    i += 1