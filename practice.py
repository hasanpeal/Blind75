from typing import Optional
from LinkedListCycle import ListNode

def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        curr = slow.next
        slow.next = None
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        slow = head
        fast = prev
        while fast:
            temp1 = slow.next
            temp2 = fast.next
            slow.next = fast
            fast.next = temp1
            slow = temp1
            fast = temp2