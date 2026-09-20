class Solution(object):
    def maximumProduct(self, nums):
        nums.sort()
        c=nums[-1]*nums[-2]*nums[-3]
        d=nums[0]*nums[1]*nums[-1]
        if c>d:
            return c
        else:
            return d