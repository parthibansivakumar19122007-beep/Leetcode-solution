class Solution(object):
    def minimumAbsDifference(self, arr):
        arr.sort()
        c=abs(arr[0]-arr[1])
        e=[]
        for i in range(len(arr)-1):
            if abs(arr[i]-arr[i+1])<c:
                c=abs(arr[i]-arr[i+1])
        for i in range(len(arr)-1):
            d=[]
            if abs(arr[i]-arr[i+1])==c:
                d.append(arr[i])
                d.append(arr[i+1])
                if d:
                    e.append(d)
       
        return e

