# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # step 1 would be to pick a head ? then choose a head.next use a temp idea
        if not list1:
            return list2
        if not list2:
            return list1
        if list1.val < list2.val:
            head =temp = list1
            temp1 = list1.next
            temp2 = list2
        else:
            head = temp = list2
            temp1 = list1
            temp2 = list2.next
        
        while temp1 and temp2:
            if temp1.val < temp2.val:
                temp.next = temp1
                temp1 = temp1.next 
            else:
                temp.next = temp2
                temp2 = temp2.next
            temp = temp.next
        if temp1:
            temp.next = temp1
        elif temp2:
            temp.next = temp2
        return head