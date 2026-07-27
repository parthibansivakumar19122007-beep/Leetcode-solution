class Solution(object):
    def searchInsert(self, nums, target):
        a=0
        for i in range(len(nums)):
            if nums[i]<target:
                a=i+1
        return a