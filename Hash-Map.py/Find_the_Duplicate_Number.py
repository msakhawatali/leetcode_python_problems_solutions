class Solution(object):
    def findDuplicate(self, nums):

        double = {}

        N = len(nums)

        for i in range(N):
            if nums[i] not in double:
                double[nums[i]] = 0
            double[nums[i]] += 1
        return max(double, key=double.get)