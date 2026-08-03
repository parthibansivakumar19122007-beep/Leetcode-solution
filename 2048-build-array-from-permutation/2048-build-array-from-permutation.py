class Solution(object):
    def buildArray(self, nums):
        c=[]
        for i in range(len(nums)):
            c.append(nums[nums[i]])
        return c