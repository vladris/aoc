inp = list(open('input').readline())
size = 25 * 6

layers = [inp[i:i + size] for i in range(0, len(inp), size)] + ['1'] * size

def top_solid(idx, start=0):
    pix = layers[start][idx]
    return pix if pix != '2' else top_solid(idx, start + 1)

img = ['#' if top_solid(i) == '1' else ' ' for i in range(size)]

for i in range(0, size, 25):
    print(''.join(img[i:i + 25]))
