class Solution(object):
    def generate(self, numRows):
        d=[]
        for i in range(numRows):
            val=1
            c=[]
            for j in range(i+1):
                c.append(val)
                val=val*(i-j)//(j+1)
            d.append(c)
        return d