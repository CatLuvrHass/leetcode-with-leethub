class Solution:

    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        cnt = 0
        for word in words:
            if self.isSubsequence(word, s):
                cnt += 1
        return cnt
    
    # from problem 392
    @lru_cache
    def isSubsequence(self, s: str, t: str) -> bool:
        """ 
        if we pass the length of s1 with index i 
        by then end of our loop
        we have a subsequence.
        """
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i+=1
            j+=1
        return i == len(s)