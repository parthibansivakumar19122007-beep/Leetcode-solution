class Solution:
    def arithmeticTriplets(self, nums: list[int], diff: int) -> int:
        a=0
        b=1
        c=2
        ans=0
        while a<len(nums) and b<len(nums) and c<len(nums):
            if nums[b]-nums[a]==diff and nums[c]-nums[b]==diff:
                ans+=1
                a+=1
                b+=1
                c+=1
            elif nums[b]-nums[a]<diff:
                b+=1
            elif nums[c]-nums[b]<diff:
                c+=1
            else:
                a+=1
        return ans
