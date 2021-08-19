# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
            
        else:
            dummy = ListNode()
            dummy.next = p1 = head
            p2 = head.next
            prev = dummy
            
            while p2:
                prev.next = p2
                p1.next = p2.next
                p2.next = p1
                
                prev = p1
                p1 = p1.next
                # list of even number
                if p1 == None:
                    break
                p2 = p1.next
                
        return dummy.next
