class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def maxdepth(root):
            if root:
                return 1+max(maxdepth(root.left),maxdepth(root.right))
            return 0
        return maxdepth(root)


