class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        m=nums[0]
        c=0
        for i in nums:
            if c<0:
                c=0
            c+=i
            if m<c:
                m=c
        return m