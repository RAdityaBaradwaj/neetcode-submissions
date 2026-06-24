# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        l3 = ListNode()
        result = l3
        carry = 0
        while l1 != None or l2!=None or carry != 0:
            l1_val = 0
            l2_val = 0
            if l1 != None:
                l1_val = l1.val
                l1 = l1.next
            if l2 != None:
                l2_val = l2.val
                l2 = l2.next

            l3.val = (l1_val + l2_val + carry) % 10
            print(l1_val,l2_val, carry, l3.val)
            carry = (l1_val + l2_val + carry) // 10
            print(carry)
            if l1 != None or l2!= None or carry != 0:
                l3.next = ListNode()
                l3 = l3.next
        
        return result