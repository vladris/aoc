goal = 633601

class Recipe:
    def __init__(self, value):
        self.value = value

e1 = Recipe(3)
e2 = Recipe(7)
e1.next, e1.prev = e2, e2
e2.next, e2.prev = e1, e1
end = e2

def found(node, goal):
    while goal:
        if node.value != goal % 10:
            return False
        node = node.prev
        goal //= 10
    return True

l = 2
while True:
    n, ds = e1.value + e2.value, []
    while n >= 10:
        ds.append(n % 10)
        n //= 10
    ds.append(n)

    for d in reversed(ds):
        new = Recipe(d)
        new.next, new.prev = end.next, end
        end.next, new.next.prev = new, new
        end = new

        l += 1

        if found(end, goal):
            print(l - len(str(goal)))
            exit()

    for _ in range(e1.value + 1):
        e1 = e1.next
    for _ in range(e2.value + 1):
        e2 = e2.next
