# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # 可以用dummy head就不用做額外處理 dummy.next 很多list都會用
        d = (l1.val + l2.val) % 10
        c = (l1.val + l2.val) // 10
        ans = ListNode(d)
        current = ans
        l1 = l1.next
        l2 = l2.next
        while l1 != None or l2 != None:
            if l1 == None:
                d = (l2.val + c) % 10
                c = (l2.val + c) // 10
                current.next = ListNode(d)
                l2 = l2.next
                #current = current.next
            elif l2 == None:
                d = (l1.val + c) % 10
                c = (l1.val + c) // 10
                current.next = ListNode(d)
                l1 = l1.next
                #current = current.next
            else:
                d = (l1.val + l2.val + c) % 10
                c = (l1.val + l2.val + c) // 10
                current.next = ListNode(d)
                l1 = l1.next
                l2 = l2.next
            current = current.next
        if c == 1:
            current.next = ListNode(1)
        return ans
