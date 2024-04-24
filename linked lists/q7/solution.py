# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def assemble_links_from_list(self, values) -> ListNode:

        if len(values) == 0:
            return 

        head = ListNode(values[0])
        cursor = head

        for i in range(1, len(values)):
            cursor.next = ListNode(values[i])
            cursor = cursor.next

        return head

    def get_whole_number_2(self, head: ListNode):
        num = 0
        cursor = head
        position = 0
        while cursor:
            num += cursor.val * (10 ** position)
            cursor = cursor.next
            position += 1

        return num

    def get_whole_number(self, head: ListNode):
        num = ""
        cursor = head
        while cursor:
            num += str(cursor.val)
            cursor = cursor.next

        return int(num[::-1])

    def solution(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> ListNode:
        a = self.get_whole_number_2(l1)
        b = self.get_whole_number_2(l2)

        sum_ = list(map(int, str(a+b)))[::-1]

        return self.assemble_links_from_list(sum_)

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        return self.solution(l1,l2)