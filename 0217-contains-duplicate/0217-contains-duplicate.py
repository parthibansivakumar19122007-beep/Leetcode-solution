class Solution(object):
    def containsDuplicate(self, nums):
        n=len(set(nums))
        if len(nums)!=n:
            return True
        else:
            return False
        