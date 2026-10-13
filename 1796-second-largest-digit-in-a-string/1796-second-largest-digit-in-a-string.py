class Solution:
    def secondHighest(self, s: str) -> int:
        c=[]
        for i in s:
            if i.isdigit():
                c.append(int(i))
        v=list(set(c))
        v.sort()
        if len(v)==1:
            return -1
        if len(v)==0:
            return -1
        else:
            return v[-2]