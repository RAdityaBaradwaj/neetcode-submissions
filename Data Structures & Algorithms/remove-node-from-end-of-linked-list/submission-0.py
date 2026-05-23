# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        traversal = head
        while traversal!=None:
            traversal = traversal.next
            count+=1
        
        count -=n
        removal = head
        while count > 1:
            removal = removal.next
            count -=1
        
        if count == 0:
            head = head.next
            return head
        removal.next = (removal.next).next

        return head
