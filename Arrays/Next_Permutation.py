class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        pivot_index = -1
        for i in range(n-2 , -1, -1):
            if nums[i] < nums[i+1]:
                pivot_index = i
                break
        if pivot_index != -1:
            for j in range(n - 1, pivot_index, -1):
                if nums[j] > nums[pivot_index]:
                    nums[pivot_index], nums[j] = nums[j], nums[pivot_index]
                    break
        left = pivot_index + 1
        right = n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1 