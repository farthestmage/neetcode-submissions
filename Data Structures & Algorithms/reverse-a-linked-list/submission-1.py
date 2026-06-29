# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Stack ??
        l1 = []
        temp = head
        if head == None or head.next == None  :
            return head
        while temp is not None:
              l1.append(temp)
              temp = temp.next 
        head = l1.pop()
        temp = head
        while l1:
            temp.next = l1.pop()
            temp = temp.next
        temp.next = None
        return head
