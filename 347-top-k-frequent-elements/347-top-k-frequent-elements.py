class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        indx, hm, res = 0, {}, []
        
        # use a hm to count freq
        for i in nums:
            if i in hm: hm[i] = hm.get(i) + 1
            else: hm[i] = 1
        
        # sort by decending order
        sorted_hm = {k: v for k, v in sorted(hm.items(), key=lambda item: -item[1])}
        
        # return the first k elements
        indx = 0
        for i in sorted_hm:
            if indx < k: res.append(i)
            indx += 1
        return res