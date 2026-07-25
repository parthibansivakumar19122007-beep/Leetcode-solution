class Solution(object):
    def maxProduct(self, n):
        n1=list(sorted(str(n)))
        return int(n1[-1])*int(n1[-2])