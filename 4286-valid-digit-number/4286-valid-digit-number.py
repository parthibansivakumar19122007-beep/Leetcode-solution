class Solution(object):
    def validDigit(self, n, x):
        n1=str(n)
        if int(n1[0])==x:
            return False
        elif str(x) not in n1:
            return False
        else:
            return True