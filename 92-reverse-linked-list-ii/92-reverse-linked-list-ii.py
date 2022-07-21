# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        """ 
        
        1 -> 2 -> 3 -> 4 -> 5
             l         r
        
        stack between l and r
        then run again, once you reach
        region between l and r
        pop and place into list
        
        1 -> *4 -> 3 -> 4 -> 5 one pass
        1 -> 4 -> *3 -> 4 -> 5 two pass
        1 -> 4 -> 3 -> *2 -> 5 three pass
        
        """ 
        st, pnter, cnt, flag = [], head, 1, False    
        
        while pnter:
            if cnt == left: flag = True
            if flag: st.append(pnter.val)
            if cnt == right: flag = False
            cnt += 1
            pnter = pnter.next
            
        pnter, cnt, flag = head, 1, False
        
        while pnter:
            if cnt == left: flag = True
            if flag and len(st)>0: 
                pnter.val = st[-1]
                st.pop()
            cnt += 1
            pnter = pnter.next
            
        return head