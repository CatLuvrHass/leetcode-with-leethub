class Solution {
    public int countVowelSubstrings(String word) {
        Set<Character> set = new HashSet<>();

        int n = word.length();
        int total = 0;
        char[] chars = word.toCharArray();
        
        for(int i = 0; i < n-4; i++){
            set.clear();
            for(int j = i; j < n; j++){
                char c = chars[j];
                if(c=='a' || c=='e' || c=='i' || c=='o' || c=='u'){
                    set.add(c);
                    if(set.size()==5)
                        total++;
                }
                else
                    break;
            }
           
        }
        
        return total;
    }
}