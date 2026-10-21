class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        a=0
        b=0
        r=[]
        while a<len(word1) and b<len(word2):
            r.append(word1[a])
            r.append(word2[b])
            a+=1
            b+=1
        if len(word1)<len(word2):
            r.append(word2[a:])
        else:
            r.append(word1[b:])
        return "".join(r)