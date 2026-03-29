# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        de = deque([root])
        while len(de) > 0:
            length = len(de)
            for i in range(length):
                node = de.popleft()
                if node.left:
                    de.append(node.left)
                if node.right:
                    de.append(node.right)
                temp = node.left
                node.left = node.right
                node.right = temp
        return root
        