# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None or head.next == None or head.next.next == None:
            return False

        hare = head
        turtle = head
        hare = hare.next.next
        turtle = turtle.next
        while hare != None and turtle != None:
            if hare == turtle:
                return True
            else:
                hare = hare.next
                if hare == None:
                    return False
                else:
                    hare = hare.next
                turtle = turtle.next
        
        return False
