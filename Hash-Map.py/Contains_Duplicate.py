class Solution(object):
    def containsDuplicate(self, nums):
        hashed = {}
        for i in nums:
            if i in hashed:
                return True
            else:
                hashed[i] = 1
        return False