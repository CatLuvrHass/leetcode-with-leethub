class Solution {
    public boolean isPowerOfFour(int n) {
        return Math.log(n)/Math.log(2) % 2 == 0;
    }
}