class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        d=[]
        n=nums
        for i in n:
            c=0
            for j in n:
                if i>j:
                    c+=1
            d.append(c)
        return d
