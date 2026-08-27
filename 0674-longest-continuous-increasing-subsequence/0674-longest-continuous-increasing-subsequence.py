class Solution(object):
    def findLengthOfLCIS(self, nums):
        c=[]
        v=1
        a=0
        b=1
        while b<len(nums):
            if nums[a]<nums[b]:
                v+=1
            else:
                c.append(v)
                v=1
            a+=1
            b+=1
        c.append(v)
        return max(c)
