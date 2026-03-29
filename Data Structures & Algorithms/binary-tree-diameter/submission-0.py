# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import math
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
    
        self.globalmax = 0
        def depth(node):
            if not node:
                return 0
            left = depth(node.left)
            right = depth(node.right)
            self.globalmax = max(self.globalmax, left + right)
        
            m = max(left, right)
            currlen = 1 + m
            return currlen
        depth(root)
        return  self.globalmax

        
        
        