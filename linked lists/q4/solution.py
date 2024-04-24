# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solution(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Uses a fast and slow pointer technique while spacing them to delete the element
        """
        fast, slow, p_cursor = head, head, None

        # Difference between the fast and slow pointers
        pointer_difference = 0
        while fast:
            # if the difference is less than n, increment the difference
            if pointer_difference < n:
                pointer_difference += 1
            # if the spacing is correct, then increment the slow cursor
            else:
                p_cursor = slow
                slow = slow.next

            # increment the fast pointer
            fast = fast.next
        
        if p_cursor is None:
            # Iter is at the beginning, delete the first
            return slow.next
        else:
            # Splice out the slow cursor
            p_cursor.next = slow.next

        return head

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        return self.solution(head, n)