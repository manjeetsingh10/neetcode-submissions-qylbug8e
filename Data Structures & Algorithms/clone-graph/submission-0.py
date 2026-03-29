"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        newroot = Node(node.val)
        cache = {node: newroot}

        q = collections.deque([node])
        
        while len(q) > 0:
            n = q.popleft()

            for neighbor in n.neighbors:
                if neighbor not in cache:
                    cache[neighbor] = Node(neighbor.val)
                    q.append(neighbor)
                
                cache[n].neighbors.append(cache[neighbor])
        return newroot
        