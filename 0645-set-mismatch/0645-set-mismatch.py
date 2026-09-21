class Solution(object):
    def findErrorNums(self, nums):
        c=set()
        d=[]
        for i in range(len(nums)):
            if nums[i] not in c:
                c.add(nums[i])
            else:
                d.append(nums[i])
        for i in range(len(nums)):
            if i+1 not in c:
                d.append(i+1)
        return d
                
