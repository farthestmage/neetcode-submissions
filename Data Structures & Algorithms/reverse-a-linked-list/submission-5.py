# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # There's a stack way then there's a recursive way then
        # Stack
        stack = []
        tempHead = head

        while tempHead != None:
            stack.append(tempHead.val)
            tempHead = tempHead.next
        newHead =temp = ListNode()
        while stack:
            temp.next = ListNode(stack.pop())
            temp = temp.next
        return newHead.next