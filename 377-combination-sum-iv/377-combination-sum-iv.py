class Solution:
	def combinationSum4(self, nums: List[int], target: int) -> int:
		#using Memoization
		dp = [-1] * target
		ans = self.solveMemo(nums,target,dp)
        
		return ans

	def solveMemo(self, nums: List[int], target: int, dp: List[int])-> int:
		count = 0
		#Base Case
		if(target == 0): return 1
		if(target < 0): return 0

		if(dp[target-1] != -1):
			return dp[target-1]

		for num in nums:
			count += self.solveMemo(nums,target-num,dp)

		dp[target-1] = count
		return dp[target-1]