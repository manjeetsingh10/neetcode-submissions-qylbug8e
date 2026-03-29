class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.result = float('-inf')
        
        def dfs(node):
            if not node:
                return 0
            
            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)
            
            # Path passing through this node
            currentPath = left + node.val + right
            
            # Update global maximum
            self.result = max(self.result, currentPath)
            
            # Return single branch to parent
            return node.val + max(left, right)
        
        dfs(root)
        return self.result
