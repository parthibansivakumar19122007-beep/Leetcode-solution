class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        d=[]
        for i in nums:
            c=0
            for j in nums:
                if i>j:
                    c+=1
            d.append(c)
        return d
