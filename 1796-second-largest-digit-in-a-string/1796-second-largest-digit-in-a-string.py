class Solution:
    def secondHighest(self, s: str) -> int:
        c=[]
        for i in s:
            if i.isdigit():
                if int(i) not in c:
                    c.append(int(i))
        # v=list(set(c))
        print(c)
        c.sort()
        if len(c)<=1:
            return -1
        # if len(c)==0:
        #     return -1
        else:
            return c[-2]