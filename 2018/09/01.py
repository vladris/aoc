elves, last = 405, 71700

class Marble:
    def __init__(self, value):
        self.value = value

current = Marble(0)
current.prev, current.next = current, current

score = [0] * elves

for i in range(1, last + 1):
    if i % 23 == 0:
        score[(i - 1) % elves] += i
        for _ in range(7):
            current = current.prev
        score[(i - 1) % elves] += current.value
        current.prev.next, current.next.prev = current.next, current.prev
        current = current.next
        continue
    new = Marble(i)
    new.prev, new.next = current.next, current.next.next
    new.prev.next, new.next.prev = new, new
    current = new

print(max(score))
