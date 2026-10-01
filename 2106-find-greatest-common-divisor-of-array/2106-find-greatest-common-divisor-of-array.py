class Solution(object):
    def findGCD(self, nums):
        n=sorted(nums)
        a,b=n[0],n[-1]
        while b!=0:
            a,b=b,a%b
        return a