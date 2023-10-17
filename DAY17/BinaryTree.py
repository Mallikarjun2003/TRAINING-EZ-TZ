class Node:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.val = key
def traverse(root):
	if  root:
		print(root.val)
		traverse(root.left)
		traverse(root.right)
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
traverse(root)
	
