# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        Result = None
        if list1 == None and list2 != None:
            return list2
        elif list1 != None and list2 == None:
            return list1
        elif list1 == None and list2 == None:
            return None
        if list1.val < list2.val:
            Result = ListNode(list1.val,None)
            list1 = list1.next
        else:
            Result = ListNode(list2.val,None)
            list2 = list2.next
        ResultHead = ListNode(0,Result)
        while list1 != None or list2 != None:
            if list1 == None:
                Result.next = list2
                return ResultHead.next
            elif list2 == None:
                Result.next = list1
                return ResultHead.next
            if list1.val < list2.val:
                Result.next = ListNode(list1.val,None)
                list1 = list1.next
            else:
                Result.next = ListNode(list2.val,None)
                list2 = list2.next
            Result = Result.next
        
        return ResultHead.next