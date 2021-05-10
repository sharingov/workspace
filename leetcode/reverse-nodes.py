# https://leetcode.com/problems/reverse-nodes-in-k-group/
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        end = beg = head
        first = True
        cloud = None
        while True:
            for _ in range(k):
                if end:
                    end = end.next
                else:
                    return head
            cur = end
            source = cloud
            cloud = beg
            for _ in range(k):
                temp = beg.next
                beg.next = cur
                cur = beg
                beg = temp
            if source is not None:
                source.next = cur
            if first:
                first = False
                head = cur
