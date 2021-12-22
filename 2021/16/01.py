inp = open("input").readline().strip()

total = 0

def parse(packet):
    global total

    ver, typ, packet = int(packet[:3], base=2), int(packet[3:6], base=2), packet[6:]
    total += ver

    return lit(packet) if typ == 4 else op(packet)

def lit(packet):
    while packet[0] == "1":
        packet = packet[5:]
    return packet[5:]

def op(packet):
    if packet[0] == "0":
        l = int(packet[1:16], base=2)
        packet = packet[16:]

        p = packet[:l]
        while p:
            p = parse(p)

        return packet[l:]
    else:
        l = int(packet[1:12], base=2)
        packet = packet[12:]

        for _ in range(l):
            packet = parse(packet)

        return packet

inp = bin(int(inp, base=16))[2:]
while len(inp) % 4:
    inp = "0" + inp

parse(inp)
print(total)
