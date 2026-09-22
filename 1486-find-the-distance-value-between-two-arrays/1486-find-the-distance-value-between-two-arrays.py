class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        c=0
        a=0
        while a<len(arr1):
            b=0
            v=True
            while b<len(arr2):
                if abs(arr1[a]-arr2[b])<=d:
                    v=False
                    break
                b+=1
            if v:
                c+=1
            a+=1
        return c