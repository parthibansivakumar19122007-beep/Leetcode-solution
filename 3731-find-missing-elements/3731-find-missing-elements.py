class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        a=min(nums)
        b=max(nums)
        s=set(nums)
        c=[]
        for i in range(a,b+1):
            if i not in s:
                c.append(i)
        return c