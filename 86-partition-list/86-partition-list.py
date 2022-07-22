# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        """
        1. make two pointers, before and after
        2. loop through and point before if smaller, else after
        3. combine two lists
        """
        # 1.
        before = before_dum = ListNode(0)
        after = after_dum = ListNode(0)
         
        # 2.
        while head:
            if head.val < x:
                before.next = head
                before = before.next
            else:
                after.next = head
                after = after.next    
            head = head.next
            
        # 3.
        after.next = None # point last point to null
        before.next = after_dum.next # point before next to dummy after
        
        return before_dum.next
            