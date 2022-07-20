class Solution:
    """
    input: string
    return : string
    func: revserse words in a string
    
    split the words, insert at index 0 each time
    """
    
    def reverseWords(self, s: str) -> str:
        words = s.split()
        string = []
        for word in words:
            string.insert(0, word)
        return " ".join(string)

        