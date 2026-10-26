class Solution:
    def reverseWords(self, s: str) -> str:
        c=[]
        x=s.split()
        for i in x:
            d=[]
            for j in i:
                d.append(j)
            c.append("".join(d[::-1]))
        return " ".join(c)