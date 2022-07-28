class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        d_s = {}
        d_t = {}
        
        for i in range(len(s)):
            d_s[s[i]] = 1 + d_s.get(s[i], 0)
            d_t[t[i]] = 1 + d_t.get(t[i], 0)
            
        return d_s == d_t