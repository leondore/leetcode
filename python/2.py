class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):
        head = ListNode(0)
        tail = head
        carry = 0

        while l1 or l2:
            num1 = num2 = 0
            if l1:
                num1 = l1.val
            if l2:
                num2 = l2.val

            sum = num1 + num2 + carry
            carry = sum // 10
            node = ListNode(sum % 10)

            tail.next = node
            tail = tail.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if carry > 0:
            tail.next = ListNode(carry)
        return head.next
