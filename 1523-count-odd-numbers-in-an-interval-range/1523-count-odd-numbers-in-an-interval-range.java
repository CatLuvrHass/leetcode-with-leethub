class Solution {
    public int countOdds(int low, int high) {
        int odds;
        odds = (high + 1) / 2 - low / 2;
        return odds;
        
    }
}