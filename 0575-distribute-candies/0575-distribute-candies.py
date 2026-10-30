class Solution:
    def distributeCandies(self, candyType: list[int]) -> int:
        a=len(set(candyType))
        return min(a,len(candyType)//2)