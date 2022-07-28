class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        add the numbers and their index to a hashmap and 
        if target - current number == a number in the hashmap
        return the indices 
        """
        d = {}
        
        for i in range(len(nums)):
            com = target - nums[i]
            if com in d:
                return [d.get(com), i]
            
            d[nums[i]] = i
        return []