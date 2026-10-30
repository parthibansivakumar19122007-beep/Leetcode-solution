class Solution:
    def distributeCandies(self, candyType: list[int]) -> int:
        a=len(candyType)//2
        b=len(set(candyType))
        return min(a,b)