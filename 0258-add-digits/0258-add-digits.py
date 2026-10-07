class Solution(object):
    def addDigits(self, num):
        while num>9:
            c=0
            # num=sum(int(i) for i in str(num))
            for i in str(num):
                c+=int(i)
            num=c
        return num