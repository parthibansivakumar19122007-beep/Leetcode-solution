class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> list[str]:
        d={}
        v1=s1.split()
        v2=s2.split()
        for i in v1:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        for i in v2:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        c=[]
        for i in d:
            if d[i]==1:
                c.append(i)
        return c