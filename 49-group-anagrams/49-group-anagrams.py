class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        each word that is anagram append to sorted key_word
        
        return the values()
        """
        anagrams = {}
        
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word not in anagrams:
                anagrams[sorted_word] = [word]
            else:
                anagrams[sorted_word].append(word)
                
        return anagrams.values()