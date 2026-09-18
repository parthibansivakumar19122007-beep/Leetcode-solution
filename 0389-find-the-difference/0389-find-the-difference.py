class Solution(object):
    def findTheDifference(self, s, t):
        a=0
        c=0
        d=0
        while a<len(t):
            c=s.count(t[a])
            d=t.count(t[a])
            if d>c:
                return t[a]
                break
            a+=1
           