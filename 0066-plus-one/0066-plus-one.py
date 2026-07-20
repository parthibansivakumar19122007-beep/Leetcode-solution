class Solution(object):
    def plusOne(self, digits):
        num="".join(map(str,digits))
        b=[]
        num1=int(num)
        num1+=1
        for i in str(num1):
            b.append(int(i))
        return b