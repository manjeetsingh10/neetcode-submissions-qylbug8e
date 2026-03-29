# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        
        dq = deque([root])

         #BFS
        while len(dq) > 0:
            r = len(dq)
            for _ in range(r):
                node = dq.popleft()
                # check if same here
                isSame = self.isSameTree(node, subRoot)
                if isSame:
                    return True
                if node:
                    dq.append(node.left)
                    dq.append(node.right)
        return False


        
        
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True

        if p and not q:
            return False
        if q and not p:
            return False

        if p.val == q.val:
            return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))
        return False