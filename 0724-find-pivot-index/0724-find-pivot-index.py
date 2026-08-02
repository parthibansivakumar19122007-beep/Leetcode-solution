class Solution(object):
    def pivotIndex(self, nums):
        t=sum(nums)
        l=0
        for i,num in enumerate(nums):
            if l==(t-l-num):
                return i
            l+=num
        return -1
