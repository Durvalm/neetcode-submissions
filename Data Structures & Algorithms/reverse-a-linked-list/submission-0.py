# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        0 : val, next
        0, 1, 2, 3
        3, 2, 1, 0


        0 -> None
        1 -> 0 -> None
        2 -> 0 -> None
        """

        prev = None
        cur = head
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
            
        return prev