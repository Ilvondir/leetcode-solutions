# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current1 = head
        current2 = head

        for _ in range(n):
            current1 = current1.next
        
        if current1 == None and n == 1:
            return None
        elif current1 == None:
            return current2.next

        while current1.next != None:
            current1 = current1.next
            current2 = current2.next
        
        current2.next = current2.next.next

        return head

        