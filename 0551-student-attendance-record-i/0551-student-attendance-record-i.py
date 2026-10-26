class Solution:
    def checkRecord(self, s: str) -> bool:
        v=s.count('A')
        x=s.count("LLL")
        if v>1 or x:
            return False
        else:
            return True