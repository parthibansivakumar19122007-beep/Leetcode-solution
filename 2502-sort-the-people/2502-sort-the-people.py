class Solution(object):
    def sortPeople(self, names, heights):
        c=[]
        for i in range(len(names)):
            d=[]
            d.append(names[i])
            d.append(heights[i])
            c.append(d)
        x=sorted(c,key=lambda c:c[1])
        y=[]
        print(x)
        for i in x:
            y.append(i[0])
        return y[::-1]
            