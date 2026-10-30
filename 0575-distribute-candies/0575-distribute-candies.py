class Solution:
    def distributeCandies(self, candyType: list[int]) -> int:
        a=len(candyType)//2
        b=len(set(candyType))
        if a>b:
            return b
        else:
            return a