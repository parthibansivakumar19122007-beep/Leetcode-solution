class Solution(object):
    def fib(self, n):
        a=0
        b=1
        c=0
        while c<n:
            a,b=b,b+a
            c+=1
        return a