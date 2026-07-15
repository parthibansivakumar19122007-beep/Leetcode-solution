class Solution(object):
    def subtractProductAndSum(self, n):
        b=1
        c=0
        while n>0:
            p=n%10
            b*=p
            c+=p
            n=n//10
        return b-c
