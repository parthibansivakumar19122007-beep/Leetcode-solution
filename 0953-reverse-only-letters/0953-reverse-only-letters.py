class Solution(object):
    def reverseOnlyLetters(self, s):
        s=list(s)
        a=0
        b=len(s)-1
        while a<b:
            if s[a].isalpha() and s[b].isalpha():
                s[a],s[b]=s[b],s[a]
                a+=1
                b-=1
            elif not s[a].isalpha():
                a+=1
            elif not s[b].isalpha():
                b-=1
        v="".join(s)
        return v