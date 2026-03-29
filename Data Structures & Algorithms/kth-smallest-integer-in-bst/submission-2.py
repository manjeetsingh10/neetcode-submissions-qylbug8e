# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result = []
        if not root:
            return -1
        result = self.find(root, result)
        return result[k-1]
        
    def find(self, node, result):
        if not node:
            return result
        
        self.find(node.left, result)
        result.append(node.val)
        self.find(node.right, result)
        return result



        