# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Step 1 reverse the other half for that we need to find the hafl
        # using fast and slow pointer we find the half 
        slow,fast = head,head

        while fast and fast.next:
            slow=slow.next
            fast = fast.next.next
        second = slow.next
        prev = slow.next = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        
        first,second = head,prev
        while first and second:
            temp1,temp2 = first.next,second.next
            first.next=second
            second.next= temp1
            first,second = temp1,temp2
        
       #return head



            