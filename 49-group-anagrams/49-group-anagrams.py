class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        def isAnagram(s):
            return sorted(s)
        
        anagrams = {}
        
        for word in strs:
            sorted_word = ''.join(isAnagram(word))
            if sorted_word not in anagrams:
                anagrams[sorted_word] = [word]
            else:
                anagrams[sorted_word].append(word)
                
        return anagrams.values()