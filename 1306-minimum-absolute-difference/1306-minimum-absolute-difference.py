class Solution(object):
    def minimumAbsDifference(self, arr):
        s=sorted(arr)
        c=[]
        d=[]
        for i in range(len(s)-1):
            x=abs(s[i]-s[i+1])
            d.append(x)
        d.sort()
        for i in range(len(s)-1):
            if abs(s[i]-s[i+1])==d[0]:
                c.append([s[i],s[i+1]])
        return c