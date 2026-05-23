# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        head = Node = ListNode()

        while lists:
            minVal = lists[0].val
            minNode = lists[0]
            minIndex = 0
            for index, node in enumerate(lists):
                if node!=None and node.val < minVal:
                    minVal = node.val
                    minNode = node
                    minIndex = index
            
            if minNode == None:
                break
            Node.next = minNode
            Node = Node.next
            lists[minIndex] = lists[minIndex].next
            if lists[minIndex] == None:
                lists.pop(minIndex)
        
        return head.next
                