# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur = dummy = ListNode()
        while list1 and list2:               
            if list1.val < list2.val:
                cur.next = list1
                list1, cur = list1.next, list1
            else:
                cur.next = list2
                list2, cur = list2.next, list2
                
        if list1 or list2:
            cur.next = list1 if list1 else list2
            
        return dummy.next

    def divide_conquer(self, lists: List[Optional[ListNode]]) -> ListNode:
        """
        Uses a recursive mergesort type of scheme to treat each linked list as an element which calls the
        merge action on each linked list
        """
        # base case, return the lists
        if len(lists) == 1:
            return lists[0]
        elif len(lists) == 0:
            return None
        else:
            # divide and conquer
            mid = len(lists)//2
            left = self.divide_conquer(lists[:mid])
            right = self.divide_conquer(lists[mid:])
            
            return self.mergeTwoLists(left,right)
    
    def solution(self, lists: List[Optional[ListNode]]):
        return self.divide_conquer(lists)

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        return self.solution(lists)
        