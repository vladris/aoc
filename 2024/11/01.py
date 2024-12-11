stones = [int(stone) for stone in open("input").read().split()]

def blink(stone, times):
    if times == 0:
        return 1

    if stone == 0:
        return blink(1, times - 1)
    s = str(stone)
    if len(s) % 2 == 0:
        return blink(int(s[:len(s) // 2]), times - 1) + blink(int(s[len(s) // 2:]), times - 1)
    return blink(stone * 2024, times - 1)


print(sum([blink(stone, 25) for stone in stones]))
