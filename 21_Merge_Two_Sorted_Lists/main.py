# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        current = dummy
        while l1 != None or l2 != None:
            if l1 == None:
                current.next = l2
                l2 = None
                break
            elif l2 == None:
                current.next = l1
                l1 = None
                break
            if l1.val > l2.val:
                current.next = ListNode(l2.val)
                current = current.next
                l2 = l2.next
            elif l1.val < l2.val:
                current.next = ListNode(l1.val)
                current = current.next
                l1 = l1.next
            else:
                current.next = ListNode(l1.val)
                current = current.next
                current.next = ListNode(l1.val)
                current = current.next
                l1 = l1.next
                l2 = l2.next
        return dummy.next
