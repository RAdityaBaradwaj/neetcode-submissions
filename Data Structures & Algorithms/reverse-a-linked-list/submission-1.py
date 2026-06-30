# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        node = head
        prev = None
        nextN = None
        while node != None:
            nextN = node.next
            node.next = prev
            prev = node
            node = nextN
        
        return prev

        