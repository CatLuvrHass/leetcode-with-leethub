class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        """
        method: bianry search n(log n)

        lo search(target) will return lower index if it finds

        search(target+1), which tells us the first index 
        where we could insert target+1, which of course 
        is one index behind the last index containing target, 
        so all I have left to do is subtract 1

        """
        def search(n):
            lo, hi = 0, len(nums)
            while lo < hi:
                mid = (lo + hi) // 2
                if nums[mid] >= n:
                    hi = mid
                else:
                    lo = mid + 1
            return lo
        lo = search(target)
        return [lo, search(target+1)-1] if target in nums[lo:lo+1] else [-1, -1]