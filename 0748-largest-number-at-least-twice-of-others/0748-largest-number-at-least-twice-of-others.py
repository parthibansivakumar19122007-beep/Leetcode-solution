class Solution(object):
    def dominantIndex(self, nums):
        n=sorted(nums)
        flag=True
        for i in range(len(nums)):
            if n[-1]==nums[i]:
                continue
            elif n[-1]<2*nums[i]:
                flag=False
                break
        if flag:
            z=nums.index(n[-1])
            return z
        else:
            return -1
