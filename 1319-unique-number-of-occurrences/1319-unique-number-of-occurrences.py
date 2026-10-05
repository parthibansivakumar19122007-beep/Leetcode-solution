class Solution(object):
    def uniqueOccurrences(self, arr):
        d={}
        for i in arr:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        c=[]
        flag=True
        for i in d:
            if d[i] not in c:
                c.append(d[i])
            else:
                flag=False
                break
        if flag:
            return flag
        else:
            return flag
