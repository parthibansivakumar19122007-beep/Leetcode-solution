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
        count=0
        for i in x:
            if count==k:
                break
            else:
                c.append(i)
                count+=1
        return c