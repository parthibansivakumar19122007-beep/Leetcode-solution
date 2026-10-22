class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        c=[]
        d={}
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        for i in d:
            if d[i]>1:
                c.append(i)
        return c