# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        current = head
        tmp = head.val
        
        while current and current.next:
            if current.next.val != tmp:
                tmp = current.next.val
                current = current.next
            elif current.next.val == tmp:
                current.next = current.next.next
                 
        return head
        
