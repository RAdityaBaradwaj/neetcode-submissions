"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = {}
        def cg(node):
            if node == None:
                return None
            nodeCopy = Node(node.val)
            visited[node] = nodeCopy
            for neighbor in node.neighbors:
                if neighbor in visited:
                    nodeCopy.neighbors.append(visited[neighbor])
                else:
                    nodeCopy.neighbors.append(cg(neighbor))

            return nodeCopy
        
        return cg(node)

