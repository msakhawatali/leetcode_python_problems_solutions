class Solution(object):
    def sortedSquares(self, nums):

        for i in range(len(nums)):
            squares = nums[i] * nums[i]
            nums[i] = squares

        return sorted(nums)
