# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        tortoise = head
        rabbit = head

        while tortoise and rabbit:
            tortoise = tortoise.next

            rabbit = rabbit.next
            if rabbit != None:
                rabbit = rabbit.next
            else:
                return False

            if tortoise == rabbit:
                return True
        
        return False