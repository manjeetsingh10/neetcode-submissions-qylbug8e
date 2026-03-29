# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        return self.printnode(root, result, 0)

    def printnode(self, node, result, depth):
        if not node:
            return result
        if depth == len(result):
            result.append(node.val)
        
        self.printnode(node.right, result, depth + 1)
        self.printnode(node.left, result, depth + 1)

        return result