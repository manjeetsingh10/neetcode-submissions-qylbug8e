# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        result = 0
        if root == None:
            return result
        return self.count(root, result, -100000)

    
    def count(self, node, result, currmax):
        if not node:
            return 0
        
        if node.val < currmax:
            return 0 + self.count(node.right, result, currmax) + self.count(node.left, result, currmax)

        currmax = max(currmax, node.val)
        # navigate
        right = self.count(node.right, result, currmax)
        left = self.count(node.left, result, currmax)

        return 1 + right + left
        
        