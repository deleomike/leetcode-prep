from copy import copy, deepcopy
import time

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def recursive(self, cursor: ListNode, prev_cursor: ListNode, depth: int) -> ListNode:
        # depth has been reached
        if depth == 0:
            cursor.next == None

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

            return self.recursive(cursor, prev_cursor, depth-1)

    def improved_reverse(self, head):
        prev = None
        current = head
        while current:
            prev, prev.next, current = current, prev, current.next
        return prev

    def recursive_start(self, head: ListNode, depth: int) -> ListNode:
        if head is None:
            return head
            
        return self.recursive(head, None, depth)

    def iterate(self, head_m: ListNode):
        cursor = head_m
        while cursor is not None:
            yield cursor
            cursor = cursor.next
        # yield None

    def insert_node(self, cursor: ListNode, node: ListNode):
        node_copy = copy(node)
        next_ = cursor.next
        cursor.next = node_copy
        node_copy.next = next_
        return cursor

    def get_length(self, head: ListNode):
        count = 0
        for cursor in self.iterate(head):
            count += 1

        return count

    def first_attempt(self, head: ListNode):
        start = time.time()
        length = self.get_length(head)
        print("get length time ", time.time() - start)
        start = time.time()
        # reversed_head = self.recursive_start(deepcopy(head), floor(length/2))
        reversed_head = self.improved_reverse(deepcopy(head))
        print("Reverse Time: ", time.time() - start)

        print(length, self.get_length(head))

        p_cursor = None
        head_iter, rev_iter = self.iterate(head), self.iterate(reversed_head)
        halfway = floor(length / 2)
        is_even = length % 2 == 0
        print("Halfway ", halfway)
        start = time.time()
        for i, (forward, rev) in enumerate(zip(head_iter, rev_iter)):
            if forward is None or rev is None:
                break
            if i >= halfway:
                # one more time
                if not is_even:
                    # print(i, forward.val, rev.val)
                    self.insert_node(forward, rev)
                    forward.next = None
                else:
                    p_cursor.next.next = None

                break

            self.insert_node(forward, rev)
            # print(i, forward.val, rev.val)
            next(head_iter)
            p_cursor = forward

        print("Merge time, ", start - time.time())

        # print(head)

    def efficient_solution(self, head: ListNode):
        """Not my solution, mine was too slow"""
        if head is None:
            return

        fast = head.next
        slow = head
        # catch the middle of the list (slow)
        # Note: This is pretty interesting, it is like a doubling iterator, where N is 2M in terms of placement
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # Cut the middle of the list and then reverse it
        rev = self.improved_reverse(slow.next)
        slow.next = None

        while rev:
            h_next = head.next
            r_next = rev.next
            head.next = rev
            rev.next = h_next
            rev = r_next
            head = h_next


    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        self.efficient_solution(head)
        # self.first_attempt(head)
        