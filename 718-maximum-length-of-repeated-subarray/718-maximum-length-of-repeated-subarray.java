class Solution {
    public int findLength(int[] A, int[] B) {
        /**
        * build a dynamic matrix of lengths, add if they matchto previous length
        * for each item in both arrays.
        */
        int max_len = 0;
        int m = A.length, n = B.length;
        
        // dp[i][j] is the length of longest common subarray ending with A[i-1], B[j-1]
        int[][] dp = new int[m + 1][n + 1];
        for(int i = 1; i <= m; i++) {
            for(int j = 1; j <= n; j++) {
                if (A[i - 1] == B[j - 1]) {
                    dp[i][j] = dp[i - 1][j - 1] + 1;
                    max_len = Math.max(max_len, dp[i][j]);
                }
            }
        }
        
        return max_len;
    }
}