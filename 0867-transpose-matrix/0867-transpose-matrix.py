class Solution(object):
    def transpose(self, matrix):
        c=[]
        for i in range(len(matrix[0])):
            d=[]
            for j in range(len(matrix)):
                d.append(matrix[j][i])
            c.append(d)
        return c