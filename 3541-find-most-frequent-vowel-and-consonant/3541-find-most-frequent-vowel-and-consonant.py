class Solution:
    def maxFreqSum(self, s: str) -> int:
        d1={}
        d2={}
        for i in s:
            if i in {'a','e','i','o','u','A','E','I','O','U'}:
                if i not in d1:
                    d1[i]=1
                else:
                    d1[i]+=1
            else:
                if i not in d2:
                    d2[i]=1
                else:
                    d2[i]+=1
        return max(d1.values(),default=0)+max(d2.values(),default=0)
        