input = "685974213"
nodes = [None] * 1000000

class Node:
    def __init__(self, value):
        self.value = value
        self.prev, self.next = None, None

root = Node(0)
n = root
for c in [int(c) for c in input]:
    n.next = Node(int(c))
    n.next.prev = n
    n = n.next
    nodes[n.value - 1] = n

for c in range(10, 1000001):
    n.next = Node(int(c))
    n.next.prev = n
    n = n.next
    nodes[n.value - 1] = n

n.next = root.next
root.next.prev = n

def step(n):
    p1, p2, p3 = n.next, n.next.next, n.next.next.next
    n.next = p3.next
    p3.next.prev = n

    m = nodes[n.value - 2]
    while m == p1 or m == p2 or m == p3:
        m = nodes[m.value - 2]

    m.next.prev = p3
    p3.next = m.next

    m.next = p1
    p1.prev = m

    return n.next

n = n.next
for c in range(10000000):
    n = step(n)

print(nodes[0].next.value * nodes[0].next.next.value)
