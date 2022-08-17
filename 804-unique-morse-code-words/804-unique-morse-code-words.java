class Solution {
    public int uniqueMorseRepresentations(String[] words) {
        
        String[] morse = new String[] {".-","-...","-.-.","-..",".",
                                "..-.","--.","....","..",".---","-.-",".-..","--",
                                "-.","---",".--.","--.-",".-.","...","-","..-",
                                "...-",".--","-..-","-.--","--.."};
        
        HashSet<String> set = new HashSet<>();
        
        for(String word: words){
            
            StringBuilder str = new StringBuilder();
            for(char l: word.toCharArray()){
                str.append(morse[(int) l - 'a']);
            }
            set.add(str.toString());
        }
        return set.size();
    }
}