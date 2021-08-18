# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = p2 = head
        p1 = dummy
        diff = 1
        
        while  p2.next:
            p2 = p2.next
            diff += 1
            
            if diff > n:
                p1 = p1.next
                diff -= 1
        
        p1.next = p1.next.next
        
        return dummy.next
        
