# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length = 0
        if not head:
            return None
        dummyHead = ListNode(0, head)
        vum = dummyHead
        slow = fast = curr = head
        while curr:
            length += 1
            curr = curr.next
        k = k % length
        m = n = length - k
        while n > 0:
            slow = slow.next
            n -= 1 
        while slow:
            vum.next = slow
            slow = slow.next
            vum = vum.next
        ss = fast
        while m > 1:
            fast = fast.next
            m -= 1
        fast.next = None
        print(ss)
        vum.next = ss
        return dummyHead.next



            
