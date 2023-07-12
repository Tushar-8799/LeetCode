# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = fast = slow = head

        if head.next is None:
            return None

        for i in range(n):
            fast = fast.next
        
        while fast:
            prev = slow
            slow = slow.next
            fast = fast.next
        
        if slow == head:
            return head.next
        
        prev.next = slow.next
        return head
