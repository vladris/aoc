goal = 633601

class Recipe:
    def __init__(self, value):
        self.value = value

e1 = Recipe(3)
e2 = Recipe(7)
e1.next = e2
e2.next = e1
end = e2

l = 2
while l < goal + 10:
    n, ds = e1.value + e2.value, []
    while n >= 10:
        ds.append(n % 10)
        n //= 10
    ds.append(n)
    l += len(ds)

    for d in reversed(ds):
        new = Recipe(d)
        new.next = end.next
        end.next = new
        end = new

    for _ in range(e1.value + 1):
        e1 = e1.next
    for _ in range(e2.value + 1):
        e2 = e2.next

curr = end.next
for _ in range(goal):
    curr = curr.next

for _ in range(10):
    print(curr.value, end="")
    curr = curr.next
