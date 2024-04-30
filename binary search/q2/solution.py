
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def LLIterator(self, head_m: ListNode):
        cursor = head_m
        while cursor is not None:
            yield cursor
            cursor = cursor.next
        yield None

    def assemble_links_from_list(self, list) -> ListNode:
        head = None

        if len(list) == 0:
            return head

        head = ListNode(list[0])
        cursor = head

        for i, val in enumerate(list):
            if i == 0:
                continue
            cursor.next = ListNode(val)
            cursor = cursor.next

        return head


    def solution(self, head_a: ListNode, head_b: ListNode):
        gen_a = self.LLIterator(head_a)
        gen_b = self.LLIterator(head_b)

        cursor_a, cursor_b = next(gen_a), next(gen_b)

        cursor = None
        head = cursor

        values = []

        while cursor_a is not None and cursor_b is not None:
            if cursor_a.val <= cursor_b.val:
                next_node = cursor_a
                cursor_a = next(gen_a)
            else:
                next_node = cursor_b
                cursor_b = next(gen_b)

            values.append(next_node.val)

        while cursor_a is not None:
            values.append(cursor_a.val)
            cursor_a = next(gen_a)

        while cursor_b is not None:
            values.append(cursor_b.val)
            cursor_b = next(gen_b)

        # print(values)
        
        return self.assemble_links_from_list(values)

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        return self.solution(list1, list2)
        