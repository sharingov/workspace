# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        check = current = head
        for i in range(n):
            check = check.next
        if not check:
            return head.next
        while check.next:
            check = check.next
            current = current.next
        current.next = None if n == 1 else current.next.next
        return head
