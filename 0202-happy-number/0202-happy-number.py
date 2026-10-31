class Solution:
    def isHappy(self, n: int) -> bool:
        seen=set()
        while True:
            c=0
            for i in str(n):
                c+=int(i)**2
            if c==1:
                return True
            if c in seen:
                return False
            seen.add(c)
            n=c
            