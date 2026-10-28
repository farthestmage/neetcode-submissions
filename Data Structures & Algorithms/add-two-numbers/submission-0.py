class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0)
        temp = head
        carryover = 0

        while l1 or l2 or carryover:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            sumx = x + y + carryover
            carryover = sumx // 10

            temp.next = ListNode(sumx % 10)
            temp = temp.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return head.next