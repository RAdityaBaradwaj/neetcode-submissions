# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head

        while fast != None and fast.next !=None:
            slow = slow.next

            fast = fast.next
            if fast != None:
                fast = fast.next

        #slow is now the midpoint
        curr = slow
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        #now prev is the reversed link list of second half

        final = Node = ListNode()
        count = 0


        while prev and head:
            if head == slow:
                break
            if count % 2 == 0:
                Node.next = head
                head = head.next
            else:
                Node.next = prev
                prev = prev.next
            Node = Node.next
            count+=1
        
        Node.next = prev or head
        head = final.next
            