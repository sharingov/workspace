# https://leetcode.com/problems/merge-k-sorted-lists/
from Queue import PriorityQueue


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeKLists(self, lists):
        head = point = ListNode(0)
        q = PriorityQueue()
        for _list in lists:
            if _list:
                q.put((_list.val, _list))
        while not q.empty():
            val, node = q.get()
            point.next = ListNode(val)
            point = point.next
            node = node.next
            if node:
                q.put((node.val, node))
        return head.next
