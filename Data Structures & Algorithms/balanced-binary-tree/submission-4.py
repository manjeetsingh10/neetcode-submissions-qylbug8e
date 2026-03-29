# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        h = self.height(root)
        if h == -1:
            return False
        return True
        
    def height(self, node):
        if not node:
            return 0
        
        left = self.height(node.left)
        if left == -1:
            return -1
        right = self.height(node.right)
        if right == -1:
            return -1
        
        diff = abs(right - left)
        if diff > 1:
            return -1
        

        return max(left, right) + 1
        