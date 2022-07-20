class Solution:
    def isSubsequence(self, s1: str, s2: str) -> bool:
        
        """ 
        if we pass the length of s1 with index i 
        by then end of our loop
        we have a subsequence.
        """
        i, j = 0, 0
        while i < len(s1) and j < len(s2):
            if s1[i] == s2[j]:
                i+=1
            j+=1
        return i == len(s1)