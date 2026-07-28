class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        c=0
        a=[]
        for i in nums:
            if i==1:
                c+=1
            else:
                a.append(c)
                c=0
        a.append(c)
        a.sort()
        print(a)
        return a[-1]        