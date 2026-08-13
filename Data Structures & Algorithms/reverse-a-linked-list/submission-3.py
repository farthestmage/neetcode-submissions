# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # How to reverse linked list ??
        # Using stack 
        stack : Optional[ListNode] = []
        temp = head
        if head == None or head.next == None:
            return head
        while temp is not None:
            stack.append(temp)
            temp = temp.next
        head = stack.pop()
        temp = head
        while stack:
            temp.next = stack.pop()
            temp = temp.next
        temp.next = None
        return head
