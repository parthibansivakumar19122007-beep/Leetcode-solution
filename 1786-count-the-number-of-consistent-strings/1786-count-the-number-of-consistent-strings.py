class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        d=0
        for i in words:
            
            for j in i:
                if j not in allowed:
                    break
            else:
                d+=1
        return d