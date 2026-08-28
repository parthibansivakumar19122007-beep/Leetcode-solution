class Solution(object):
    def isPalindrome(self, s):
        v=s.lower()
        u="".join(x for x in v if x.isalnum())
        a=0
        b=len(u)-1
        p=True
        while a<len(u):
            if u[a]==u[b]:
                a+=1
                b-=1
            else:
                p=False
                break
        return p