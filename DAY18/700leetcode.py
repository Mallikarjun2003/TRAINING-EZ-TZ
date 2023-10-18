from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
#This solution is achieved by while loop.


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        temp = root
        while(temp):
            if temp.val > val:
                temp = temp.left
            elif temp.val < val:
                temp = temp.right
            else:
                return temp 
        return None
#the other Solution can be achieved with the recursion.
'''
            
            # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None
        if root.val == val:
            return root
        if root.val > val:
            return self.searchBST(root.left,val)
        elif root.val < val:
            return self.searchBST(root.right,val) 
            
            '''