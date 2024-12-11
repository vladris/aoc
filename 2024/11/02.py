stones = [int(stone) for stone in open("input").read().split()]

cache = {}
def blink(stone, times):
    if times == 0:
        return 1

    if (stone, times) in cache:
        return cache[(stone, times)]

    if stone == 0:
        cache[(stone, times)] = blink(1, times - 1)
        return cache[(stone, times)]
    s = str(stone)
    if len(s) % 2 == 0:
        cache[(stone, times)] = blink(int(s[:len(s) // 2]), times - 1) + blink(int(s[len(s) // 2:]), times - 1)
        return cache[(stone, times)]
    
    cache[(stone, times)] = blink(stone * 2024, times - 1)
    return cache[(stone, times)]


print(sum([blink(stone, 75) for stone in stones]))
