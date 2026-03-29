# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        return self.getMax(root)

    def getMax(self, node):
        if not node:
            return 0
        
        return max(self.getMax(node.left), self.getMax(node.right)) + 1
