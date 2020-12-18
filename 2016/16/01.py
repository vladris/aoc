data = "10001110011110000"

while len(data) < 272:
    data += "0" + "".join(["1" if c == "0" else "0" for c in reversed(data)])

data = data[:272]

def checksum(data):
    checksum = ""
    for i in range(0, len(data), 2):
        checksum += "1" if data[i] == data[i + 1] else "0"
    return checksum

while True:
    data = checksum(data)
    if len(data) % 2 == 1:
        print(data)
        exit()
