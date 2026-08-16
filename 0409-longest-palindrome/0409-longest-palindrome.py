class Solution(object):
    def longestPalindrome(self, s):
        ans=0
        for i in set(s):
            n=s.count(i)
            ans+=(n//2)*2
        if ans<len(s):
            ans+=1
        return ans