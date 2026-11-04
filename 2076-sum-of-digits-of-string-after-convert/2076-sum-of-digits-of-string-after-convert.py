class Solution:
    def getLucky(self, s: str, k: int) -> int:
        d={'a':'1','b':'2', 'c':'3', 'd':'4', 'e':'5', 'f':'6', 'g':'7', 'h':'8', 'i':'9', 'j':'10', 'k':'11', 'l':'12', 'm':'13', 'n':'14', 'o':'15', 'p':'16', 'q':'17', 'r':'18', 's':'19', 't':'20', 'u':'21', 'v':'22', 'w':'23', 'x':'24', 'y':'25', 'z':'26'}
        c=""
        for i in s:
            c=c+d[i]
        v=0
        while k>0:
            x=0
            for j in c:
                x+=int(j)
            v=x
            c=str(v)
            k-=1
        return v