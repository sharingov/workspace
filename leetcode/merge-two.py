# https://leetcode.com/problems/merge-two-sorted-lists/
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        p = ans = ListNode()
        while l1 and l2:
            p.next = ListNode()
            p = p.next
            if l1.val < l2.val:
                p.val = l1.val
                l1 = l1.next
            else:
                p.val = l2.val
                l2 = l2.next
        x = l1 or l2
        while x:
            p.next = ListNode()
            p = p.next
            p.val = x.val
            x = x.next
        return ans.next
