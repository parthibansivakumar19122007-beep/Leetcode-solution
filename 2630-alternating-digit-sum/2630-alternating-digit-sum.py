class Solution(object):
    def alternateDigitSum(self, n):
        c=0
        num=list(map(int,str(n)))
        for i in range(len(num)):
            if i%2==0:
                c+=num[i]
            else:
                c-=num[i]
            print(i)
        return c