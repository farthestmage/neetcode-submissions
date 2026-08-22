# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        setx = set()
        tempHead= head

        while tempHead:
            if tempHead in setx:
                return True
            setx.add(tempHead)
            tempHead = tempHead.next
        return False