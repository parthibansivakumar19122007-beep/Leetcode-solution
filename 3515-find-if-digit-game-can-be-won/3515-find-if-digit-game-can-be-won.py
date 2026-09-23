class Solution(object):
    def canAliceWin(self, nums):
        s=str(nums)
        c=0
        d=0
        for i in nums:
            if i<10:
                c+=i
            else:
                d+=i
        if c==d:
            return False
        else:
            return True
