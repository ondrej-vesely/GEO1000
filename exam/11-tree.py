class Node:
    def __init__(self, val, left=None, right=None):
        self.value = val
        self.left = left
        self.right = right

tree = Node(10, Node(4, Node(1), Node(7)), Node(16, Node(13),Node(19)))

def size_recu(t):
    left = size_recu(t.left) if t.left else 0
    right = size_recu(t.right) if t.right else 0
    return 1 + left + right

print(size_recu(tree))

