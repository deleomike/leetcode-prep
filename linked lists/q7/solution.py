# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def solution(self, head: Optional[ListNode]) -> bool:
        fast, slow = head, head

        while fast:
            if fast.next is None:
                return False
                
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                return True

        return False
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        return self.solution(head)
        