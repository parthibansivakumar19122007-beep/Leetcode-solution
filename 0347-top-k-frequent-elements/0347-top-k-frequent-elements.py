class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        d={}
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        x=dict(sorted(d.items() ,key=lambda x:x[1],reverse=True))
        c=[]
        for i in x:
            if len(c)==k:
                break
            else:
                c.append(i)
        return c