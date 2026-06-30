# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        l1 = head
        l2 = head.next
        while l2 and l2.next:
            l1 = l1.next
            l2 = l2.next.next

        node = l1.next
        prev = l1.next = None
        nextN = None

        while node != None:
            nextN = node.next
            node.next = prev
            prev = node
            node = nextN
        
        first, second = head, prev
        
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first,second =tmp1,tmp2
        

                