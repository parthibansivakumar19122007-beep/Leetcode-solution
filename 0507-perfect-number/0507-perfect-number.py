class Solution(object):
    def checkPerfectNumber(self, num):
        if num<=1:
            return False
        flag=1
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                flag+=i
                if i !=num//i:
                    flag+=num//i
        if num==flag:
            return True
        else:
            return False