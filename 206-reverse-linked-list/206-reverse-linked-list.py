# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        """
        1 -> 2 -> 3 -> 4 -> 5 ->
        
        p    c    n
        """
        prev, cur = None, head
        
        while cur:
            nxt = cur.next # save the next
            cur.next = prev # make the switch
            prev = cur # move prev
            cur = nxt # proceed to next
        
        return prev
            