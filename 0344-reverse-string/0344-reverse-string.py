class Solution(object):
    def reverseString(self, s):
        a=0
        b=len(s)-1
        while a<=b:
            s[a],s[b]=s[b],s[a]
            a+=1
            b-=1
        return s
        