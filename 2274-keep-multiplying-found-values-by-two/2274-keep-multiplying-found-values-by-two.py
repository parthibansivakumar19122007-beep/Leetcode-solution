class Solution(object):
    def findFinalValue(self, nums, original):
        while True:
            if original not in nums:
                return original
            else:
                original=2*original