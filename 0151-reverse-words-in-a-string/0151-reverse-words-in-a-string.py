class Solution:
    def reverseWords(self, s: str) -> str:
        v=list(s.split())
        a=0
        b=len(v)-1
        while a<b:
            v[a],v[b]=v[b],v[a]
            a+=1
            b-=1
        
        return " ".join(v)