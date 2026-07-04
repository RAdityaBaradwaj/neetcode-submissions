# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        node = head
        lefthead = None
        dummy = ListNode(0,head)
        k = 1
        while k != left:
            if k+1 == left:
                lefthead = node
            node = node.next
            k+=1
        prev = lefthead
        leftnum = node
        while k != right:
            k+=1
            temp = node.next
            node.next = prev
            prev = node
            node = temp
        temp = node.next
        node.next = prev
        prev = node
        node = temp
        leftnum.next = node
        if lefthead != None:
            lefthead.next = prev
        else:
            dummy.next = prev
        return dummy.next