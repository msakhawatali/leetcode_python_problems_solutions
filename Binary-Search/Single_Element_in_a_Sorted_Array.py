class Solution(object):
    def singleNonDuplicate(self, nums): 
        n = len(nums)
        if n == 1: return nums[0]
        if nums[0] != nums[1]: return nums[0]
        if nums[n-1] != nums[n-2]: return nums[n-1]
        st = 0
        end = n-1
        while st <= end:
            mid = int(st + (end-st)/2)
            if nums[mid] != nums[mid-1] and nums[mid] != nums[mid+1]:
                return nums[mid]
            if mid % 2 == 0:
                if nums[mid-1] == nums[mid]:
                    end = mid - 1
                else:
                    st = mid + 1
            else:
                if nums[mid-1] == nums[mid]:
                    st = mid + 1
                else:
                    end = mid - 1
        