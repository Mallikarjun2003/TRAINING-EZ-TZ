from collections import deque

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def bfs_traverse(root):
    if root is None:
        return

    queue = deque()
    queue.append(root)

    while queue:
        node = queue.popleft()
        print(node.val)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)

bfs_traverse(root)
