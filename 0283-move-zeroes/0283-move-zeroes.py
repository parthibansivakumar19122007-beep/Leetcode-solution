class Solution(object):
    def moveZeroes(self, nums):
        a=0
        b=0
        while b<len(nums):
            if nums[b]!=0:
                nums[a],nums[b]=nums[b],nums[a]
                b+=1
                a+=1
            else:
                b+=1
        return nums