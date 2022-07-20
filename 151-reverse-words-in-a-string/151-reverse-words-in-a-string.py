class Solution:
    """
    input: string
    return : string
    func: revserse words in a string
    
    first we reverse the stirng fully
    then we move to each gap in the string
    and re-reverse the strings to their 
    correct state
    """
    def reverseWords(self, s: str) -> str:
        reversed_message = self.reverse_characters(s, 0, len(s)-1)
        
        current_index = 0
        for i in range(len(reversed_message) + 1):
            
            if(i == len(reversed_message) or reversed_message[i] == ' '):
                reversed_message = self.reverse_characters(reversed_message, current_index, i - 1)
                current_index = i + 1
                
        # deals with some edge cases
        string = ''.join(reversed_message)
        cleanedStr = ' '.join(string.split())
        
        return cleanedStr
            
    """
    input : string
    return : char array
    func: reverse a string.
    
    left and right pointer, and swap
    """
    def reverse_characters(self, message, l, r):  
        s = list(message)
        while l < r:

            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        return s

        