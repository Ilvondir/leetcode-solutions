# Definition for singly-linked list.

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        current1 = l1.next
        current2 = l2.next
        result = ListNode((l1.val + l2.val) % 10)
        current_result = result
        transfer = (l1.val + l2.val) // 10

        while True:

            if current1 != None and current2 != None:
                current_result.next = ListNode((current1.val + current2.val + transfer) % 10)
                transfer = (current1.val + current2.val + transfer) // 10

                current1 = current1.next
                current2 = current2.next
            elif current1 != None and current2 == None:
                current_result.next = ListNode((current1.val + transfer) % 10)
                transfer = (current1.val + transfer) // 10

                current1 = current1.next
            elif current1 == None and current2 != None:
                current_result.next = ListNode((current2.val + transfer) % 10)
                transfer = (current2.val + transfer) // 10

                current2 = current2.next
            else:
                if transfer > 0: current_result.next = ListNode(transfer)
                break

            current_result = current_result.next

        return result
    

num1 = ListNode(2, ListNode(4, ListNode(3)))
num2 = ListNode(5, ListNode(6, ListNode(4)))
sol = Solution()
print(sol.addTwoNumbers(num1, num2))