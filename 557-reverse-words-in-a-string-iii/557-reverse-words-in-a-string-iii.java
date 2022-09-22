class Solution {
    public String reverseWords(String s) {
        char[] sentence = s.toCharArray();
        for (int i = 0; i < sentence.length; i++){        
            // get each word
            if(sentence[i] != ' '){ 
                int j = i;
                // get the full word
                while (j + 1 < sentence.length && sentence[j + 1] != ' '){ j++; } 
                reverseWord(sentence, i, j);
                i = j;
            }
            
        }
        return new String(sentence);
        
    }
    public void reverseWord(char[] a, int i, int j){
        
        for(; i < j; i++, j--){
            char temp = a[i];
            a[i] = a[j];
            a[j] = temp;
        }
        
    }
}