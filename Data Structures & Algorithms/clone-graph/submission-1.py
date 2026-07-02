"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        hashMap = {}

        def cloneG(node):
            if node == None:
                return None
            nonlocal hashMap
            if node.val in hashMap:
                return hashMap[node.val]
            newNode = Node(node.val)

            hashMap[node.val] = newNode
            for n in node.neighbors:
                newNode.neighbors.append(cloneG(n))

            return newNode
        
        return cloneG(node)


            