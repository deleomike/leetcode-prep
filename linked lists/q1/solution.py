from copy import copy

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def recursive(self, cursor: ListNode, prev_cursor: ListNode) -> ListNode:
        # If this is the last node
        if cursor.next is None:
            # Set the next node as the previous node
            cursor.next = prev_cursor
            # Return the last node
            return cursor
        else:
            # Every other case

            # for some node, Assign the prior

            # Copy the cursor
            cursor_copy = copy(cursor)

            # Assign next to be the prior node
            cursor.next = prev_cursor

            # Set the prev cursor from the current cursor
            prev_cursor = cursor
            
            # Iterate this cursor to be the next node
            cursor = cursor_copy.next

            return self.recursive(cursor, prev_cursor)


    def recursive_start(self, head: ListNode) -> ListNode:
        if head is None:
            return head
            
        return self.recursive(head, None)

    def iterative(self, head: ListNode) -> ListNode:

        cursor = head
        prev_cursor = None

        while cursor != None:
            # For this current node

            # Copy the cursor
            cursor_copy = copy(cursor)

            # Assign next to be the prior node
            cursor.next = prev_cursor

            # Set the prev cursor from the current cursor
            prev_cursor = cursor
            
            # Iterate this cursor to be the next node
            cursor = cursor_copy.next

        # Return the prev cursor which is the last nod
        return prev_cursor

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.recursive_start(head)
        # sol = self.iterative(head)
        # return sol
        