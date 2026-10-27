class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        d=0
        for i in stones:
            if i in jewels:
                d+=1
        return d