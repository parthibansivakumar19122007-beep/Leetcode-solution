class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        w=sum(nums[:k])
        m=w/k
        for i in range(k,len(nums)):
            w=w-nums[i-k]+nums[i]
            m=max(m,w/k)
        return m