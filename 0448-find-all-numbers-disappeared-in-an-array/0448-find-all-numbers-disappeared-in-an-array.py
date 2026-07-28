class Solution(object):
    def findDisappearedNumbers(self, nums):
        b=set(nums)
        c=[]
        for i in range(1,len(nums)+1):
            if i not in b:
                c.append(i)
        return c
