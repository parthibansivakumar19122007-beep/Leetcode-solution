class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        c=[]
        d={}
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                c.append(i)
        return c