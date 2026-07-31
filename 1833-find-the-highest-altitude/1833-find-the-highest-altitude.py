class Solution(object):
    def largestAltitude(self, gain):
        a=0
        b=0
        for i in gain:
            a+=i
            if a>b:
                b=a
        return b
