from functools import reduce

inp = open("input").readline().strip()

def parse(packet):
    ver, typ, packet = int(packet[:3], base=2), int(packet[3:6], base=2), packet[6:]

    return lit(packet) if typ == 4 else op(packet, typ)

def lit(packet):
    val = ""
    while packet[0] == "1":
        val += packet[1:5]
        packet = packet[5:]
    val += packet[1:5]
    return packet[5:], int(val, base=2)

def op(packet, typ):
    values = []

    if packet[0] == "0":
        l = int(packet[1:16], base=2)
        packet = packet[16:]

        p = packet[:l]
        while p:
            p, v = parse(p)
            values.append(v)

        packet = packet[l:]
    else:
        l = int(packet[1:12], base=2)
        packet = packet[12:]

        for _ in range(l):
            packet, v = parse(packet)
            values.append(v)

    match typ:
        case 0: return packet, sum(values)
        case 1: return packet, reduce(lambda x, y: x * y, values)
        case 2: return packet, min(values)
        case 3: return packet, max(values)
        case 5: return packet, int(values[0] > values[1])
        case 6: return packet, int(values[0] < values[1])
        case 7: return packet, int(values[0] == values[1])

inp = bin(int(inp, base=16))[2:]

while len(inp) % 4:
    inp = "0" + inp

print(parse(inp)[1])
