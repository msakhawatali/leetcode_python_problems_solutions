class Solution(object):
    def moveZeroes(self, nums):
        index = 0
        for num in nums:
            if num != 0:
                nums[index] = num
                index += 1
        for i in range(index, len(nums)):
            nums[i] = 0
        return nums