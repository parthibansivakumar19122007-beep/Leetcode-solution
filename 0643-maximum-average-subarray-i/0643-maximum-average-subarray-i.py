class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        w=sum(nums[:k])
        m=w/k
        for i in range(k,len(nums)):
            w=w-nums[i-k]+nums[i]
            if w/k>m:
                m=w/k
        return m