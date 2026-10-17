class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        a=min(nums)
        b=max(nums)
        c=[]
        for i in range(a,b+1):
            if i not in set(nums):
                c.append(i)
        return c