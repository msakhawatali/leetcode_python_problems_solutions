class Solution(object):
    def removeElement(self, nums, val):
        if not nums:
            return 0
        st =0
        while st < len(nums):
            if nums[st] == val:
                nums.remove(val)
                continue
            st += 1
        return len(nums) 