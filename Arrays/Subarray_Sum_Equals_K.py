class Solution(object):
    def subarraySum(self, nums, k):

        prefix_dict = {}
        prefix_dict[0] = 1
        result, cumSum = 0, 0
        n = len(nums)

        for i in range(n):
            cumSum += nums[i]

            if cumSum-k in prefix_dict:
                result += prefix_dict[cumSum-k]

            prefix_dict[cumSum] = prefix_dict.get(cumSum, 0) + 1
            
        return result