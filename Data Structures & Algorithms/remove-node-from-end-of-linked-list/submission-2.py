# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # have the length of the list ?? fast and slow pointer .. ?? O(n)
        #countprev and new 
        fast,slow = head,head 
        for i in range(n):
            fast =fast.next
        if slow.next == None:
            head = None
            return head
        while slow:
            if fast ==None:
                head = slow.next
                return head
            if fast.next == None:
                slow.next = slow.next.next
                return head
            slow = slow.next
            fast = fast.next
        return head
