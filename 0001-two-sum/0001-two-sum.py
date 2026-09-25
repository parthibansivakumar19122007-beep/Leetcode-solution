class Solution:
    def twoSum(self, nums, target):
        a=0
        b=len(nums)-1
        num=sorted(nums)
        while a<b:
            if num[a]+num[b]==target:
                v=nums.index(num[a])
                nums[v]=-1
                s=nums.index(num[b])
                return [v,s]
            elif num[a]+num[b]>target:
                b-=1
            elif num[a]+num[b]<target:
                a+=1
                
