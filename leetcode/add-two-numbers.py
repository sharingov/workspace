class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode()
        current = result
        remainder = 0
        while l1 or l2 or remainder:
            val = remainder
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
            remainder = val // 10
            current.next = ListNode(val % 10)
            current = current.next
        return result.next

if __name__ == '__main__':
    a = ListNode(2, ListNode(4, ListNode(3)))
    b = ListNode(5, ListNode(6, ListNode(4)))
    s = Solution()
    x = s.addTwoNumbers(a, b)
    print(x.val, x.next.val, x.next.next.val)
