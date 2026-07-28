class Solution(object):
    def isPalindrome(self, s):
        v=s.lower()
        u="".join(x for x in v if x.isalnum())
        return u==u[::-1]