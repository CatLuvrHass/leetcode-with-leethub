class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set, longest = set(nums), 0
        
        for n in nums:
            # check if its the start of a sequence
            if (n - 1) not in num_set:
                length = 1
                while (n + length) in num_set:
                    length += 1
                longest = max(length, longest)
        return longest
                