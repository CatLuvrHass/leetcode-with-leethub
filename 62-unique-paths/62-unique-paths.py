class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        a top-down approach
        
        accumulate the sum of paths
        from top-down and left-right
        
        """
        def paths(i, j, memo={}):
            if (i, j) in memo: return memo[i, j]
            if i == 0 or j == 0: memo[i, j] = 1 # since we can only move down or right along the x and y axis is 1
            else: memo[i, j] = paths(i-1, j, memo) + paths(i, j-1, memo) # current path to this point = right and top square accumulated sum 
            return memo[i, j]
        
        return paths(m-1, n-1) # return the number of paths to the bottom-righ corner