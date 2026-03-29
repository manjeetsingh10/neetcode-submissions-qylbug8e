# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indexMap = {v:i for i,v in enumerate(inorder)}
        self.counter = 0

        def construct(left, right):
            if left > right:
                return None
            
            nodeVal = preorder[self.counter]
            nodeIndex = indexMap.get(nodeVal)
            self.counter += 1
            
            node = TreeNode(nodeVal)
            node.left = construct(left, nodeIndex-1)
            node.right = construct(nodeIndex + 1, right)
            return node

        return construct(0, len(inorder) - 1)