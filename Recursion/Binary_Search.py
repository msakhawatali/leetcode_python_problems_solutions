class Solution(object):
    def binSearch(self, nums, tar, st, end):
        mid = st + (end - st)/2
    
        if st > end:
            return -1

        if nums[mid] == tar:
            return mid
        elif nums[mid] < tar:
            return self.binSearch(nums, tar, mid + 1, end)
        else:
            return self.binSearch(nums, tar, st, mid - 1)


    def search(self, nums, tar):
        return self.binSearch(nums, tar, 0, len(nums)-1)

        