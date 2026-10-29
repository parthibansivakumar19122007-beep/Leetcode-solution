class Solution:
    def frequencySort(self, nums: list[int]) -> list[int]:
        d={}
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        x=dict(sorted(d.items(),key=lambda x:(x[1],-x[0])))
        c=[]
        print(x)
        for i in x:
            for j in range(x[i]):
                c.append(i)
        return c