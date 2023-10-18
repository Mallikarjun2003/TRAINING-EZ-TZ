class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        temp = root
        parent = root
        if not root:
            root = TreeNode(val)
            return root
        while(temp):
            parent = temp
            if temp.val > val:
                temp = temp.left
            elif temp.val < val:
                temp = temp.right
            
        if parent.val > val:
            parent.left = TreeNode(val)
        else:
            parent.right = TreeNode(val)
        return root
