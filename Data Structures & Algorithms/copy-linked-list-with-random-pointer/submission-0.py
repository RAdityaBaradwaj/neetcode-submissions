"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nodemap = {}

        node = head
        while node:
            nodemap[node] = Node(node.val)
            node = node.next

        nodemap[None] = None
        
        newHead = nodemap[head]

        node = newHead

        while node:
            node.next = nodemap[head.next]
            node.random = nodemap[head.random]
            head = head.next
            node = node.next
        
        return newHead