# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        Can we solve this if we just keep breaking the list after k nodes
        reversing both of them, then connecting them?

        is there a more clever way to do it?
        I don't think so...

        Apparently we'll reverse the 2 lists, then reconnect them.
        The point is how to store and know what to reconnect.
        And how to know if we should reverse or not the last list, which might not contain k characters.

        It's always the head of the first list (which becomes the tail after reversing),
        that connects with the tail of the second list (which becomes the head after reversing)
        """

        cur = head
        lsts = []
        remaining = []
        # 1 - first loop to go from k to k and separate the lists
        while cur:
            tmp = []
            count = 0
            while cur and count < k:
                tmp.append(cur)
                cur = cur.next
                count += 1
            if count == k:
                lsts.append(tmp)
            else:
                remaining = tmp

        # If there are no complete groups of k
        if len(lsts) == 0:
            return head
            
        # 2 - Reverse each complete group
        reversed_lsts = []

        for lst in lsts:
            cur = lst[0]
            prev = None
            count = 0

            # Reverse exactly k nodes
            while cur and count < k:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
                count += 1

            # prev is now the head of this reversed group
            reversed_lsts.append(prev)

        # 3 - Connect the reversed groups
        for i in range(len(lsts) - 1):
            # lsts[i][0] was the original head
            # after reversing, it is now the tail
            lsts[i][0].next = reversed_lsts[i + 1]

        # 4 - Connect the last reversed group
        # to the remaining unreversed nodes
        last_tail = lsts[-1][0]

        if remaining:
            last_tail.next = remaining[0]
        else:
            last_tail.next = None

        # First reversed group's head is the new head
        return reversed_lsts[0]



                

