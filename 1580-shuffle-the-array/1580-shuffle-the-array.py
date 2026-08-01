class Solution(object):
    def shuffle(self, nums, n):
        c=[]
        d=[]
        for i in range(len(nums)):
            if i<n:
                c.append(nums[i])
            else:
                d.append(nums[i])
        e=[]
        for i in range(len(c)):
            e.append(c[i])
            e.append(d[i])
        return e