from math import ceil

class Node:
    def __init__(self, value=None, left=None, right=None):
        self.value, self.left, self.right = value, left, right
        self.parent = None

def parse(inp):
    if inp[0].isdigit():
        return Node(value=int(inp[0])), inp[1:]

    left, inp = parse(inp[1:])
    right, inp = parse(inp[1:])

    result = Node(left=left, right=right)
    left.parent, right.parent = result, result

    return result, inp[1:]

def add(node1, node2):
    result = Node(value=None, left=node1, right=node2)
    result.left.parent, result.right.parent = result, result
    return result

def explode(node, depth=0):
    if node.value != None:
        return False

    if node.left.value != None and node.right.value != None and depth > 3:
        p = node
        while p.parent and p.parent.left == p:
            p = p.parent
        if p.parent:
            p = p.parent.left
            while p.value == None:
                p = p.right
            p.value += node.left.value

        p = node
        while p.parent and p.parent.right == p:
            p = p.parent
        if p.parent:
            p = p.parent.right
            while p.value == None:
                p = p.left
            p.value += node.right.value

        node.value = 0
        node.left, node.right = None, None
        return True

    return explode(node.left, depth + 1) or explode(node.right, depth + 1)

def split(node):
    if node.value == None:
        return split(node.left) or split(node.right)

    if node.value < 10:
        return False

    node.left = Node(value=node.value // 2)
    node.right = Node(value=ceil(node.value / 2.0))
    node.left.parent, node.right.parent = node, node
    node.value = None
    return True

def reduce(node):
    while explode(node) or split(node):
        pass

    return node

def magnitude(node):
    if node.value != None:
        return node.value

    return 3 * magnitude(node.left) + 2 * magnitude(node.right)

n = [parse(line.strip())[0] for line in open("input").readlines()]

while len(n) > 1:
    n = [reduce(add(n[0], n[1]))] + n[2:]

print(magnitude(n[0]))
